import pytest

from maya import cmds

import mayax as mx


def test_should_getInstance_given_node_and_attributeName():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'translate')


def test_should_getInstance_given_nodeName_and_attributeName():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute('transform1', 'translate')
    assert mx.Attribute(node.uniqueName, 'translate')


def test_should_getInstance_given_attributeFullName():
    mx.Node(cmds.createNode('transform', name='node'))
    assert mx.Attribute('node.translate')


def test_should_getInstance_given_transformNodeName_and_shapeAttributeName():
    locatorName = cmds.spaceLocator()[0]
    assert mx.Attribute(locatorName, 'localPositionX')


def test_should_getInstance_given_arrayAttributeName():
    node = mx.Node(cmds.createNode('multMatrix'))
    assert mx.Attribute(node, 'matrixIn')
    assert mx.Attribute(node, 'matrixIn').type == 'TdataCompound'


def test_should_getInstance_given_arrayAttributeName_and_index():
    node = mx.Node(cmds.createNode('multMatrix'))
    assert mx.Attribute(node, 'matrixIn[0]')


def test_should_raiseMayaNodeError_given_nonexistentNodeName():
    with pytest.raises(mx.MayaNodeError):
        assert mx.Attribute('nonexistentNode', 'translate')


def test_should_raiseMayaAttributeError_given_onlyNodeName():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        assert mx.Attribute(node.uniqueName)


def test_should_raiseMayaAttributeError_given_nonexistentAttributeName():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        assert mx.Attribute(node.uniqueName, 'nonexistentAttrName')


def test_should_raiseAttributeError_given_nonexistentAttributeName():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(AttributeError):
        assert mx.Attribute(node.uniqueName, 'nonexistentAttrName')
