from maya import cmds

import mayax as mx


def test_should_undoManyOperationsAtOnce():
    @mx.undoable
    def createCubes():
        cmds.polyCube()
        cmds.polyCube()
        cmds.polyCube()

    createCubes()
    assert len(cmds.ls(type='polyCube')) == 3
    cmds.undo()
    assert not cmds.ls(type='polyCube')
