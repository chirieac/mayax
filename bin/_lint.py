"""Lint the code."""

import os
import colorama


def main():
    """Run linting commands."""
    print('\n=== pylint: mayax =============================================================\n')
    pylint1 = os.system('pylint src/mayax')
    print('\n=== pylint: tests =============================================================\n')
    pylint2 = os.system('pylint tests')

    print('\n=== pycodestyle: mayax ========================================================\n')
    pycodestyle1 = os.system('pycodestyle src/mayax')
    print('\n=== pycodestyle: tests ========================================================\n')
    pycodestyle2 = os.system('pycodestyle tests')

    print('\n=== pydocstyle: mayax =========================================================\n')
    pydocstyle1 = os.system('pydocstyle src/mayax')
    print('\n=== pydocstyle: tests =========================================================\n')
    pydocstyle2 = os.system('pydocstyle tests')

    print('\n===============================================================================\n')

    colorama.init()

    print(
        'pylint: {}mayax ({}){}, {}tests ({})'.format(
            colorama.Fore.RED if pylint1 else colorama.Fore.GREEN,
            'FAIL' if pylint1 else 'OK',
            colorama.Fore.RESET,
            colorama.Fore.RED if pylint2 else colorama.Fore.GREEN,
            'FAIL' if pylint2 else 'OK',
        )
    )

    print(colorama.Fore.RESET)

    print(
        'pycodestyle: {}mayax ({}){}, {}tests ({})'.format(
            colorama.Fore.RED if pycodestyle1 else colorama.Fore.GREEN,
            'FAIL' if pycodestyle1 else 'OK',
            colorama.Fore.RESET,
            colorama.Fore.RED if pycodestyle2 else colorama.Fore.GREEN,
            'FAIL' if pycodestyle2 else 'OK',
        )
    )

    print(colorama.Fore.RESET)

    print(
        'pydocstyle: {}mayax ({}){}, {}tests ({})'.format(
            colorama.Fore.RED if pydocstyle1 else colorama.Fore.GREEN,
            'FAIL' if pydocstyle1 else 'OK',
            colorama.Fore.RESET,
            colorama.Fore.RED if pydocstyle2 else colorama.Fore.GREEN,
            'FAIL' if pydocstyle2 else 'OK',
        )
    )


if __name__ == '__main__':
    main()
