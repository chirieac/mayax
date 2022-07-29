from maya import cmds

import mayax as mx


def test_should_addReferenceAttribute_given_type():
    node = mx.Node(cmds.createNode('network'))
    assert mx.Attribute(node, 'refAttr', type='message')
    assert mx.Attribute(node, 'refAttr')
    assert mx.Attribute(node, 'refAttr').type == 'message'


def test_should_addReferenceAttribute_given_pyType():
    node = mx.Node(cmds.createNode('network'))
    assert mx.Attribute(node, 'refAttr', type=mx.Node)
    assert mx.Attribute(node, 'refAttr')
    assert mx.Attribute(node, 'refAttr').type == 'message'


def test_should_addReferenceAttribute_given_node():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    assert mx.Attribute(metaNode, 'refAttr', node)
    assert mx.Attribute(metaNode, 'refAttr')
    assert mx.Attribute(metaNode, 'refAttr').type == 'message'
    assert (
        cmds.connectionInfo(
            '{}.refAttr'.format(metaNode.uniqueName),
            sourceFromDestination=True,
        )
        == '{}.message'.format(node.uniqueName)
    )


def test_should_addReferenceAttribute_given_nodeName_and_pyType():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    assert mx.Attribute(metaNode, 'refAttr', node.uniqueName, type=mx.Node)
    assert mx.Attribute(metaNode, 'refAttr')
    assert mx.Attribute(metaNode, 'refAttr').type == 'message'
    assert (
        cmds.connectionInfo(
            '{}.refAttr'.format(metaNode.uniqueName),
            sourceFromDestination=True,
        )
        == '{}.message'.format(node.uniqueName)
    )


# --------------------------------------------------------------------------------------------------


def test_should_getNoneReference_given_unreferencedAttribute():
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', type=mx.Node)
    assert attr.value is None


def test_should_getNodeInstance_given_referencedAttribute():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', node)
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node


# --------------------------------------------------------------------------------------------------


def test_should_setUnreferencedAttribute_given_node():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', type=mx.Node)
    assert attr.value is None
    attr.value = node
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node


def test_should_setUnreferencedAttribute_given_nodeName():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', type=mx.Node)
    assert attr.value is None
    attr.value = node.uniqueName
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node


def test_should_setUnreferencedAttribute_given_noneType():
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', type=mx.Node)
    assert attr.value is None
    attr.value = None
    assert attr.value is None


def test_should_setReferencedAttribute_given_node():
    node1 = mx.Node(cmds.createNode('transform'))
    node2 = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', node1)
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node1
    assert attr.value != node2
    attr.value = node2
    assert attr.value == node2
    assert attr.value != node1


def test_should_setReferencedAttribute_given_nodeName():
    node1 = mx.Node(cmds.createNode('transform'))
    node2 = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', node1.uniqueName, type=mx.Node)
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node1
    assert attr.value != node2
    attr.value = node2.uniqueName
    assert attr.value == node2
    assert attr.value != node1


def test_should_setReferencedAttribute_given_noneType():
    node = mx.Node(cmds.createNode('transform'))
    metaNode = mx.Node(cmds.createNode('network'))
    attr = mx.Attribute(metaNode, 'refAttr', node)
    assert isinstance(attr.value, mx.Node)
    assert attr.value == node
    attr.value = None
    assert attr.value is None
