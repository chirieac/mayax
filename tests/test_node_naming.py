import pytest

from maya import cmds

import mayax as mx


def test_should_getName():
    cmds.createNode('transform')
    assert mx.Node('transform1').name == 'transform1'


def test_should_getName_given_dgNode():
    assert mx.Node('lambert1').name == 'lambert1'


def test_should_getName_given_nodeWithNonUniqueName():
    cmds.createNode('transform', name='parent1')
    cmds.createNode('transform', name='child', parent='parent1')
    cmds.createNode('transform', name='parent2')
    cmds.createNode('transform', name='child', parent='parent2')
    assert mx.Node('parent1|child').name == 'child'


def test_should_getUniqueName():
    cmds.createNode('transform', name='parent1')
    cmds.createNode('transform', name='child', parent='parent1')
    node = mx.Node('child')

    assert node.name == 'child'
    assert node.uniqueName == 'child'

    cmds.createNode('transform', name='parent2')
    cmds.createNode('transform', name='child', parent='parent2')

    assert node.name == 'child'
    assert node.uniqueName == 'parent1|child'


def test_should_setName():
    cmds.createNode('transform')
    node = mx.Node('transform1')
    assert node.name == 'transform1'
    node.name = 'group'
    assert node.name == 'group'


def test_should_setNameUsingRenameMethod():
    cmds.createNode('transform')
    node = mx.Node('transform1')
    assert node.name == 'transform1'
    node.rename('group')
    assert node.name == 'group'


def test_should_renameUsingExtraFlags():
    cmds.polyCube()
    cube = mx.Node('pCube1')
    cubeShape = mx.Node('pCubeShape1')

    assert cube.name == 'pCube1'
    assert cubeShape.name == 'pCubeShape1'

    cube.rename('Cube', ignoreShape=True)

    assert cube.name == 'Cube'
    assert cubeShape.name == 'pCubeShape1'


def test_should_raiseMayaNodeError_when_nodeBecomesInvalid():
    cmds.createNode('transform')
    node = mx.Node('transform1')
    cmds.delete('transform1')
    with pytest.raises(mx.MayaNodeError):
        node.name = 'newName'
