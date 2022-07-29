from maya import cmds

import mayax as mx


def test_should_compareNode_given_self():
    node = mx.Node(cmds.createNode('transform'))
    nodeSelf = node
    assert node == nodeSelf
    assert not bool(node != nodeSelf)


def test_should_compareNode_given_sameNode():
    node = mx.Node(cmds.createNode('transform'))
    sameNode = mx.Node(node.uniqueName)
    assert node == sameNode
    assert not bool(node != sameNode)


def test_should_compareNode_given_sameNodeName():
    node = mx.Node(cmds.createNode('transform'))
    assert node == node.uniqueName
    assert not bool(node != node.uniqueName)


def test_should_compareNode_given_differentNode():
    node1 = mx.Node(cmds.createNode('transform'))
    node2 = mx.Node(cmds.createNode('transform'))
    assert node1 != node2
    assert not bool(node1 == node2)


def test_should_compareNode_given_differentNodeName():
    node1 = mx.Node(cmds.createNode('transform'))
    node2 = mx.Node(cmds.createNode('transform'))
    assert node1 != node2.uniqueName
    assert not bool(node1 == node2.uniqueName)


def test_should_compareNode_given_nonexistentNodeName():
    node = mx.Node(cmds.createNode('transform'))
    assert node != 'nonexistentNodeName'
    assert not bool(node == 'nonexistentNodeName')


def test_should_compareNode_given_nonUniqueNodeName():
    mx.Node(cmds.createNode('transform', name='parent1'))
    mx.Node(cmds.createNode('transform', name='child', parent='parent1'))
    mx.Node(cmds.createNode('transform', name='parent2'))
    mx.Node(cmds.createNode('transform', name='child', parent='parent2'))

    assert mx.Node('parent1|child') != 'child'


def test_should_compareNode_given_object():
    node = mx.Node(cmds.createNode('transform'))
    obj = object()
    assert node != obj
    assert not bool(node == obj)


def test_should_compareNode_given_similarObject():
    # This that NotImplemented is returned in the equality functions for unknown objects.
    class CustomObject(object):
        def __eq__(self, other):
            return True

        def __ne__(self, other):
            return False

    node = mx.Node(cmds.createNode('transform'))
    obj = CustomObject()
    assert node == obj
    assert not bool(node != obj)
