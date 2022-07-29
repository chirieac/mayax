"""pytest fixtures."""

import pytest

from maya import cmds


@pytest.fixture(autouse=True)
def mayaEmptyScene():
    cmds.file(newFile=True, force=True)


@pytest.fixture
def scenePath(tmpdir):
    return '{}/scene.ma'.format(tmpdir)
