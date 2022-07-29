"""Drop this file in a Maya viewport to install MayaX."""

import os
import sys

from maya import cmds


def onMayaDroppedPythonFile(*_):
    """Install when the file is dropped in the viewport."""
    rootPath = os.path.dirname(os.path.realpath(__file__))
    sourcePath = os.path.join(rootPath, 'src')
    mayaModulesPath = os.path.normpath(
        os.path.join(
            cmds.internalVar(userAppDir=True),
            cmds.about(version=True),
            'modules',
        )
    )
    moduleFilename = os.path.join(mayaModulesPath, 'mayax.mod')

    if sourcePath not in sys.path:
        sys.path.append(sourcePath)

    from mayax import __version__

    if not os.path.exists(mayaModulesPath):
        os.makedirs(mayaModulesPath)

    with open(moduleFilename, mode='w') as moduleFile:
        moduleContent = '\n'.join(
            [
                '+ MayaX {} {}'.format(__version__, rootPath),
                'scripts: src',
            ]
        )

        moduleFile.write(moduleContent)

    cmds.confirmDialog(
        title='MayaX',
        message='MayaX was installed.',
        button='OK',
        icon='information',
    )
