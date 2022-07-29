from maya import cmds


# Every test should run within an empty Maya scene -------------------------------------------------


def test_should_createPolyCube():
    assert cmds.polyCube()


def test_should_haveEmptyScene():
    assert not cmds.ls(type='polyCube')


# --------------------------------------------------------------------------------------------------
