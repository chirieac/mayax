"""Test the code using the Maya's Python interpreter (mayapy)."""

import os
import sys

SRC_DIR = os.environ['SRC_DIR']
PYTEST_LOCATION = os.environ['PYTEST_LOCATION']
PYTEST_TEMP_DIR = os.environ['PYTEST_TEMP_DIR']
MAYA_APP_DIR = os.environ['MAYA_APP_DIR']


def main():
    """Prepare the testing environment."""
    sys.path.append(SRC_DIR)
    sys.path.append(PYTEST_LOCATION)
    sys.path.append(MAYA_APP_DIR)

    runTests(sys.argv[1:])


def runTests(args):
    """Run the tests."""
    import pytest
    import maya.standalone

    with open(os.path.join(MAYA_APP_DIR, 'userSetup.py'), 'w') as setupFile:
        setupFile.write(
            '\n'.join(
                [
                    'from maya import cmds',
                    'cmds.loadPlugin("quatNodes")',
                ]
            )
        )

    maya.standalone.initialize(name='mayax_test')

    result = pytest.main(['--basetemp', PYTEST_TEMP_DIR] + args)

    maya.standalone.uninitialize()

    sys.exit(result)


if __name__ == '__main__':
    main()
