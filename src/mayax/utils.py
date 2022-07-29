"""Utility functions that makes working with Maya easier."""

import os

from maya import cmds


def getCurrentProjectDirectory():
    """Return the path for the selected project directory."""
    return cmds.workspace(query=True, rootDirectory=True)


def getModulesDirectory():
    """Return the path for the modules directory."""
    return os.path.normpath(
        os.path.join(
            cmds.internalVar(userAppDir=True),
            cmds.about(version=True),
            'modules',
        )
    )
