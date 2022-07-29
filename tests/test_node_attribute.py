import pytest

from maya import cmds

import mayax as mx


def test_should_getAttribute():
    node = mx.Node(cmds.createNode('transform'))
    assert isinstance(node['translate'], mx.Attribute)


def test_should_deleteAttribute():
    node = mx.Node(cmds.createNode('transform', name='testNode'))
    cmds.addAttr(node.name, longName='testAttr')

    assert cmds.attributeQuery('testAttr', node='testNode', exists=True)

    node.deleteAttr('testAttr')

    assert not cmds.attributeQuery('testAttr', node='testNode', exists=True)


def test_should_returnAttribute_when_adding():
    node = mx.Node(cmds.createNode('transform'))
    attr = node.addAttr('testAttr', 'test')
    assert isinstance(attr, mx.Attribute)


def test_should_checkAttributeExistence_given_existingAttributeName():
    node = mx.Node(cmds.createNode('transform'))
    assert node.hasAttr('translate')


def test_should_checkAttributeExistence_given_nonexistingAttributeName():
    node = mx.Node(cmds.createNode('transform'))
    assert not node.hasAttr('nonexistentAttrName')


def test_should_checkAttributeExistence_given_arrayAttributeName():
    node = mx.Node(cmds.createNode('multMatrix'))
    assert node.hasAttr('matrixIn')


def test_should_checkAttributeExistence_given_arrayAttributeName_and_index():
    node = mx.Node(cmds.createNode('multMatrix'))
    assert node.hasAttr('matrixIn[0]')


def test_should_magicallyGetAttribute():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 10.5, 1.0, node.uniqueName)
    assert node.translateX == 15.0
    assert node.translateY == 10.5
    assert node.translateZ == 1.0
    assert node.visibility


def test_should_magicallySetAttribute():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 0.0, 0.0, node.uniqueName)
    assert node['translateX'].value == 15
    assert node['visibility'].value
    node.translateX = 10
    node.visibility = False
    assert node['translateX'].value == 10
    assert not node['visibility'].value


def test_should_setClassAttribute_given_conflictingNames():
    node = mx.Node(cmds.createNode('transform'))
    node.testAttr = 'test'
    cmds.addAttr(node.uniqueName, longName='testAttr', dataType='string')
    cmds.setAttr('{}.testAttr'.format(node.uniqueName), 'empty', type='string')
    assert node.testAttr == 'test'
    assert node['testAttr'].value == 'empty'
    node.testAttr = 'dumbo'
    assert node.testAttr == 'dumbo'
    assert node['testAttr'].value == 'empty'


def test_should_setClassAttribute_given_conflictingPropertyNames():
    node = mx.Node(cmds.createNode('transform'))

    cmds.addAttr(node.uniqueName, longName='name', dataType='string')
    cmds.setAttr('{}.name'.format(node.uniqueName), 'empty', type='string')

    assert node.name == 'transform1'
    assert node['name'].value == 'empty'

    node.name = 'dumbo'

    assert node.name == 'dumbo'
    assert node['name'].value == 'empty'


def test_should_raiseMayaNodeError_given_insufficientArguments_when_addingAttribute():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaNodeError):
        node.addAttr('testAttr')
