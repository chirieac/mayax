"""Generate the wrapping for the maya.cmds."""

import os
import sys
import re
import json
import urllib.request
import textwrap
import colorama
from bs4 import BeautifulSoup


ARG_GEN_DATA = 'data'

CACHE_DOCS = True
CACHE_DIR = '__gencmd_cache__'

CMDS_URL = 'http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/'

CMDS_MOD_DESCRIPTION = 'Wrap `maya.cmds` to accept and return instances of `Node`.'
CMDS_MOD_PATH = 'src/mayax/cmd.py'
CMDS_DATA_PATH = 'cmd_data.json'


# --------------------------------------------------------------------------------------------------


def main(args):
    """Script execution entry point."""
    kwargs = parseCommandLineArguments(args)

    if ARG_GEN_DATA in kwargs:
        generateCommandsData()
    else:
        generateCommandsModule()


def parseCommandLineArguments(args):
    """Parse command line arguments and return a dictionary."""
    kwargs = {}

    for arg in args:
        argParts = arg.split('=')

        key = argParts[0]
        value = argParts[1] if len(argParts) == 2 else None

        kwargs[key] = value

    return kwargs


def generateCommandsModule():
    """Generate the wrapped commands module."""
    commandsData = getCommandsData()

    if not commandsData:
        printCommandsDataNotFoundWarning()
        return

    commands = commandsData['commands']
    obsoluteCommands = []

    with open(CMDS_MOD_PATH, 'w', encoding='utf-8') as cmdFile:
        cmdFile.write(f'"""{CMDS_MOD_DESCRIPTION}"""\n\n')

        cmdFile.write('# AUTO-GENERATED. Use `bin/gencmd` to update.\n')
        cmdFile.write(
            '# pylint: disable=redefined-builtin,too-many-lines,too-complex,too-many-branches\n\n'
        )

        cmdFile.write('from maya import cmds\n\n')
        cmdFile.write('from .node import Node, MayaNodeError\n')
        cmdFile.write('from .attribute import Attribute, MayaAttributeError\n')
        cmdFile.write('from .strtype import STR_TYPE\n')

        cmdFile.write(f'\n\n{getWrapFunction()}\n')

        for cmd in commands:
            if cmd['obsolete']:
                obsoluteCommands.append(cmd['name'])
                continue

            wrappedCmd = wrapCommand(cmd)

            cmdFile.write(wrappedCmd)

    commandsCount = len(commands) - len(obsoluteCommands)

    print(f'{colorama.Fore.GREEN}-------\nSUCCESS\n-------')
    print(f'{colorama.Fore.LIGHTGREEN_EX}Commands generated: {commandsCount}')
    print(f'{colorama.Fore.LIGHTBLUE_EX}Obsolute commands ignored: {len(obsoluteCommands)}')
    print(f'{obsoluteCommands}{colorama.Fore.RESET}')


def generateCommandsData():
    """Generate the commands data for doing the wrapping."""
    commands = getAllCommands()
    commandsData = {'commands': commands}

    saveCommandsData(commandsData)

    print(f'{colorama.Fore.GREEN}-------\nSUCCESS\n-------')
    print(f'{colorama.Fore.LIGHTGREEN_EX}Commands saved: {len(commands)}{colorama.Fore.RESET}')


# --------------------------------------------------------------------------------------------------


def getCommandsData():
    """Get the commands from the data file."""
    try:
        with open(CMDS_DATA_PATH, 'r', encoding='utf-8') as dataFile:
            return json.load(dataFile)
    except IOError:
        return None
    except (KeyError, ValueError):
        print(f'{colorama.Fore.RED}Invalid commands data file!{colorama.Fore.RESET}')

        sys.exit()


def saveCommandsData(data):
    """Save the commands data to a file."""
    with open(CMDS_DATA_PATH, 'w', encoding='utf-8') as dataFile:
        json.dump(data, dataFile, indent=4, sort_keys=True, separators=(',', ': '))

        dataFile.write('\n')


def printCommandsDataNotFoundWarning():
    """Print a warning if no commands data file was found."""
    print(
        f'{colorama.Fore.YELLOW}No commands data found. '
        f'Run `{__file__} {ARG_GEN_DATA}`.{colorama.Fore.RESET}'
    )


def getCommandHtml(cmdName):
    """Get the command's HTML documentation."""
    html = ''

    if CACHE_DOCS:
        try:
            with open(f'{CACHE_DIR}/{cmdName}.html', 'r', encoding='utf-8') as cachedFile:
                html = cachedFile.read()
        except IOError:
            pass

    if not html:
        with urllib.request.urlopen(f'{CMDS_URL}{cmdName}.html') as url:
            html = url.read().decode()

        if CACHE_DOCS:
            if not os.path.exists(CACHE_DIR):
                os.makedirs(CACHE_DIR)

            with open(f'{CACHE_DIR}/{cmdName}.html', 'w', encoding='utf-8') as cachedFile:
                cachedFile.write(html)

    return html


def getAllCommands():
    """Get a list of all commands."""
    html = getCommandHtml('index_all')
    parser = BeautifulSoup(html, features="html.parser")

    commands = []

    for tag in parser.find_all('a'):
        cmdName = tag['href'].replace('.html', '')
        cmdInfo = getCommandInfo(cmdName)

        commands.append(cmdInfo)

        print(cmdName)

    return commands


def getCommandInfo(cmdName):
    """Get the command info."""
    cmdInfo = {
        'name': cmdName,
        'description': '',
        'synopsis': '',
        'categories': [],
        # 'flags': [],
        'returnTypes': [],
        'obsolete': False,
    }

    html = getCommandHtml(cmdName)

    cmdInfo['obsolete'] = getCommandObsolete(html, cmdName)

    if cmdInfo['obsolete']:
        return cmdInfo

    cmdInfo['categories'] = getCommandCategories(html)
    cmdInfo['description'] = getCommandDescription(html)
    cmdInfo['synopsis'] = getCommandSynopsis(html)
    # cmdInfo['flags'] = getCommandFlags(html)
    cmdInfo['returnTypes'] = getCommandReturnTypes(html)

    return cmdInfo


def getCommandObsolete(html, cmdName):
    """Get the command's obsolete state."""
    parser = BeautifulSoup(html, features="html.parser")

    if parser.find(string=re.compile(rf'{cmdName} \(Obsolete\)')):
        return True

    return False


def getCommandDescription(html):
    """Get the command's description."""
    description = ''

    startCut = '<h2><a name="hSynopsis">Synopsis</a></h2>'
    endCut = '<h2><a name="hReturn">Return value</a></h2>'

    html = html[html.find(startCut) + len(startCut) :]
    html = html[: html.find(endCut)]

    parser = BeautifulSoup(html, features="html.parser")

    parser.find(id='synopsis').decompose()
    parser.find('p').decompose()

    description = str(parser)

    description = [x.strip() for x in description.split('\n\n') if x][0]
    description = [x.strip() for x in description.split('<p></p>') if x][0]

    description = stripHtml(description)
    description.strip()

    description = description.split('.')[0].strip() + '.'

    return description


def getCommandCategories(html):
    """Get the command's categories test."""
    categories = []

    parser = BeautifulSoup(html, features="html.parser")

    for tag in parser.find(id='banner').find_all('a', href=re.compile('^cat')):
        categories.append(tag.string)

    return categories


def getCommandFlags(html):
    """Get the command's flags."""
    flags = []

    parser = BeautifulSoup(html, features="html.parser")

    flagsEl = parser.find('a', attrs={'name': 'hFlags'})

    if not flagsEl:
        return flags

    flagsTable = flagsEl.parent.find_next_sibling('table')

    for row in flagsTable.find_all('tr', attrs={'bgcolor': '#EEEEEE'}):
        data = row.find_all('td')
        flagNames = data[0].find_all('b')
        descriptionTable = row.find_next_sibling().find('table')

        description = descriptionTable.find_all('td')[1].decode_contents()

        description = stripHtml(description)
        description = description.split('.')[0].strip() + '.'

        flags.append(
            {
                'description': description,
                'longName': flagNames[0].decode_contents().strip(),
                'shortName': flagNames[1].decode_contents().strip(),
                'type': data[1].find('i').decode_contents().strip(),
            }
        )

    return flags


def getCommandReturnTypes(html):
    """Get the command's return types."""
    returnTypes = []

    parser = BeautifulSoup(html, features="html.parser")

    returnTypesContainer = parser.find('a', attrs={'name': 'hReturn'}).parent.find_next_sibling()

    if returnTypesContainer.name != 'table':
        return returnTypes

    for returnTypeRowEl in returnTypesContainer.find_all('tr'):
        data = returnTypeRowEl.find_all('td')

        returnType = data[0].find('i').string
        description = data[1].decode_contents().strip()

        description = stripHtml(description)

        returnTypes.append(
            {
                'description': description,
                'type': returnType,
            }
        )

    return returnTypes


def getCommandSynopsis(html):
    """Get the command's synopsis."""
    parser = BeautifulSoup(html, features="html.parser")

    synopsis = parser.find(id='synopsis').find('code').decode_contents().strip()

    synopsis = cleanText(synopsis)

    synopsis = re.sub(r'<a href="(.*?)">(.*?)</a>', r'\2', synopsis)
    synopsis = re.sub(r'<i>(.*?)</i>', r'\1', synopsis)

    return synopsis


def getCommandExamples(html):
    """Get the command's examples."""
    parser = BeautifulSoup(html, features="html.parser")

    examplesEl = parser.find('a', attrs={'name': 'hExamples'}).parent.find_next_sibling('pre')

    return examplesEl.decode_contents()


def cleanText(text):
    """Clean spaces, new lines, tabs, etc."""
    return ' '.join(text.split())


def stripHtml(html):
    """Strip HTML from text and replace it with reStructuredText."""
    html = cleanText(html)

    html = re.sub(r'<b>(.*?)</b>', r'`\1`', html)
    html = re.sub(r'<strong>(.*?)</strong>', r'`\1`', html)
    html = re.sub(r'<i>(.*?)</i>', r'`\1`', html)
    html = re.sub(r'<em>(.*?)</em>', r'`\1`', html)
    html = re.sub(r'<tt>(.*?)</tt>', r'`\1`', html)

    html = re.sub(r'<pre>(.*?)</pre>', r'``\1``', html)
    html = html.replace('<pre>', '')

    html = html.replace('<p></p>', '')

    html = cleanText(html)

    html = html.replace('<br/>', '\n')

    html = stripHtmlList(html)

    return html.strip()


def stripHtmlList(html, innerPosition=0):
    """Strip HTML list from text and replace it with reStructuredText."""
    parser = BeautifulSoup(html, features="html.parser")

    listEl = parser.find(('ul', 'ol'))

    if not listEl:
        return html

    listTag = listEl.name
    listIndex = html.find(f'<{listTag}')
    listContent = ''

    if not innerPosition:
        listContent += '\n'

    orderedListSeq = 1

    for listItem in listEl.find_all('li', recursive=False):
        innerListEl = listItem.find(('ul', 'ol'))
        innerListHtml = ''

        if innerListEl:
            innerListHtml = str(innerListEl)
            innerListEl.decompose()

        itemContent = listItem.decode_contents().strip()

        if itemContent:
            listContent += '\n{}{} {}'.format(
                ' ' * 4 * innerPosition,
                f'{orderedListSeq}.' if listTag == 'ol' else '-',
                itemContent,
            )

        if innerListHtml:
            listContent += stripHtmlList(innerListHtml, innerPosition + 1)

        if listTag == 'ol':
            orderedListSeq += 1

    if not innerPosition:
        listContent += '\n\n'

    listEl.decompose()

    html = str(parser)

    html = html[:listIndex] + listContent + html[listIndex:]

    parser = BeautifulSoup(html, features="html.parser")

    if parser.find(('ul', 'ol')):
        return stripHtmlList(html)

    return html


# --------------------------------------------------------------------------------------------------


def getWrapFunction():
    """Get the wrap function used to wrap the commands."""
    return (
        'def _wrapCommand(cmdFn, args, kwargs):\n'
        '    args = [\n'
        '        value.uniqueName if isinstance(value, Node)\n'
        '        else value.fullName if isinstance(value, Attribute)\n'
        '        else value\n'
        '        for value in args\n'
        '    ]\n'
        '\n'
        '    for k in kwargs:\n'
        '        if isinstance(kwargs[k], Node):\n'
        '            kwargs[k] = kwargs[k].uniqueName\n'
        '        elif isinstance(kwargs[k], list):\n'
        '            kwargs[k] = [\n'
        '                value.uniqueName if isinstance(value, Node) else value\n'
        '                for value in kwargs[k]\n'
        '            ]\n'
        '\n'
        '    result = cmdFn(*args, **kwargs)\n'
        '\n'
        '    if isinstance(result, STR_TYPE):\n'
        '        try:\n'
        '            if result.find(\'.\') != -1:\n'
        '                result = Attribute(result)\n'
        '            else:\n'
        '                result = Node(result)\n'
        '        except (MayaNodeError, MayaAttributeError):\n'
        '            pass\n'
        '    elif isinstance(result, list):\n'
        '        for i, value in enumerate(result):\n'
        '            if not isinstance(value, STR_TYPE):\n'
        '                continue\n'
        '\n'
        '            try:\n'
        '                if value.find(\'.\') != -1:\n'
        '                    result[i] = Attribute(value)\n'
        '                else:\n'
        '                    result[i] = Node(value)\n'
        '            except (MayaNodeError, MayaAttributeError):\n'
        '                pass\n'
        '\n'
        '    return result'
    )


def wrapCommand(cmd):
    """Wrap the command."""
    # flags = ''
    # for flag in cmd['flags']:
    #     flags += (
    #         '    {} ({}) : {}\n'
    #         '        {}\n'
    #     ).format(
    #         flag['longName'],
    #         flag['shortName'],
    #         flag['type'],
    #         wrapText(flag['description'], width=90, subsequentIndent=' ' * 8),
    #     )

    return (
        '\n\n'
        'def {0}(*args, **kwargs):  # noqa\n'
        '    """{1}\n'
        '\n'
        '    {2}\n'
        '\n'
        '    {3}\n'
        '    """\n'
        '    return _wrapCommand(cmds.{0}, args, kwargs)\n'
    ).format(
        cmd['name'],
        wrapText(cmd['description'], width=90, subsequentIndent=' ' * 4),
        wrapText(cmd['synopsis'], width=90, subsequentIndent=' ' * 4),
        f'{CMDS_URL}{cmd["name"]}.html',
    )


def wrapText(text, width, initialIndent='', subsequentIndent=''):
    """Wrap text to fit `width`, keeping new lines."""
    return '\n'.join(
        [
            textwrap.fill(
                line.strip(),
                width=width,
                initial_indent=subsequentIndent if i else initialIndent,
                subsequent_indent=subsequentIndent,
            ).replace(
                '\n', '\n  ' if line.startswith('- ') else '\n'
            )  # reStructuredText list
            for i, line in enumerate(text.splitlines())
        ]
    )


# --------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main(sys.argv[1:])
