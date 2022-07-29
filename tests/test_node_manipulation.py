from maya import cmds

import mayax as mx


def test_should_deleteNodeFromScene():
    cmds.createNode('transform')
    assert cmds.ls('transform1')
    mx.Node('transform1').delete()
    assert not cmds.ls('transform1')


def test_should_duplicateNode():
    cmds.createNode('transform')
    assert cmds.ls('transform1')
    assert not cmds.ls('transform2')
    duplicatedNode = mx.Node('transform1').duplicate()
    assert isinstance(duplicatedNode, mx.Node)
    assert cmds.ls('transform1')
    assert cmds.ls('transform2')


def test_should_duplicateNode_given_name():
    cmds.createNode('transform')
    assert cmds.ls('transform1')
    assert not cmds.ls('duplicatedTransform')
    duplicatedNode = mx.Node('transform1').duplicate(name='duplicatedTransform')
    assert isinstance(duplicatedNode, mx.Node)
    assert cmds.ls('transform1')
    assert cmds.ls('duplicatedTransform')


def test_should_selectNode():
    cmds.createNode('transform')
    cmds.createNode('transform')
    cmds.select(clear=True)
    assert not cmds.ls(selection=True)
    mx.Node('transform1').select()
    assert len(cmds.ls(selection=True)) == 1
    assert cmds.ls(selection=True)[0] == 'transform1'


def test_should_addNodeToActiveSelection():
    cmds.createNode('transform')
    cmds.createNode('transform')
    assert len(cmds.ls(selection=True)) == 1
    assert cmds.ls(selection=True)[0] == 'transform2'
    mx.Node('transform1').select(add=True)
    assert len(cmds.ls(selection=True)) == 2
    assert cmds.ls(selection=True)[0] == 'transform2'
    assert cmds.ls(selection=True)[1] == 'transform1'
