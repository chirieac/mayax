from maya import cmds

import mayax as mx


def test_should_getName():
    node = mx.Node(cmds.createNode('transform'))

    assert mx.Attribute(node, 'translate').name == 'translate'


def test_should_getFullName():
    node = mx.Node(cmds.createNode('transform'))

    assert mx.Attribute(node, 'translate').fullName == 'transform1.translate'


def test_should_getNode():
    node = mx.Node(cmds.createNode('transform'))

    assert mx.Attribute(node, 'translate').node == node


def test_should_getType():
    node = mx.Node(cmds.createNode('transform'))

    cmds.addAttr(node.uniqueName, longName='testAttr', dataType='string')

    assert mx.Attribute(node, 'testAttr').type == 'string'
    assert mx.Attribute(node, 'visibility').type == 'bool'
    assert mx.Attribute(node, 'translate').type == 'double3'
    assert mx.Attribute(node, 'translateX').type == 'doubleLinear'
    assert mx.Attribute(node, 'scaleX').type == 'double'


def test_should_getLockedState():
    node = mx.Node(cmds.createNode('transform'))

    assert not mx.Attribute(node, 'visibility').locked

    cmds.setAttr('{}.visibility'.format(node.uniqueName), lock=True)

    assert mx.Attribute(node, 'visibility').locked


def test_should_setLockedState():
    node = mx.Node(cmds.createNode('transform'))

    mx.Attribute(node, 'visibility').locked = True

    assert cmds.getAttr('{}.visibility'.format(node.uniqueName), lock=True)

    mx.Attribute(node, 'visibility').locked = False

    assert not cmds.getAttr('{}.visibility'.format(node.uniqueName), lock=True)


def test_should_getKeyableState():
    node = mx.Node(cmds.createNode('transform'))

    assert mx.Attribute(node, 'visibility').keyable

    cmds.setAttr('{}.visibility'.format(node.uniqueName), keyable=False)

    assert not mx.Attribute(node, 'visibility').keyable


def test_should_setKeyableState():
    node = mx.Node(cmds.createNode('transform'))

    mx.Attribute(node, 'visibility').keyable = True

    assert cmds.getAttr('{}.visibility'.format(node.uniqueName), keyable=True)

    mx.Attribute(node, 'visibility').keyable = False

    assert not cmds.getAttr('{}.visibility'.format(node.uniqueName), keyable=True)


def test_should_getChannelBoxState():
    node = mx.Node(cmds.createNode('transform'))

    assert not mx.Attribute(node, 'visibility').channelBox

    cmds.setAttr('{}.visibility'.format(node.uniqueName), channelBox=True)

    assert mx.Attribute(node, 'visibility').channelBox


def test_should_setChannelBoxState():
    node = mx.Node(cmds.createNode('transform'))

    mx.Attribute(node, 'visibility').channelBox = True

    assert cmds.getAttr('{}.visibility'.format(node.uniqueName), channelBox=True)

    mx.Attribute(node, 'visibility').channelBox = False

    assert not cmds.getAttr('{}.visibility'.format(node.uniqueName), channelBox=True)
