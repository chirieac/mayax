from maya import cmds

import mayax as mx


def test_should_checkNodeExistence_given_validNode():
    node = mx.Node(cmds.polyCube(name='theCube')[0])

    assert node.exists


def test_should_checkNodeExistence_given_deletedNode():
    node = mx.Node(cmds.polyCube(name='theCube')[0])

    cmds.delete('theCube')

    assert not node.exists


def test_should_getNodeType():
    node = mx.Node(cmds.createNode('multMatrix'))
    assert node.type == 'multMatrix'
