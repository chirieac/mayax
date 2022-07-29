import pytest

from maya import cmds

import mayax as mx


def test_should_connectAttribute():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translateY')
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    assert not sourceAttr.value
    assert not destinationAttr.value
    sourceAttr.connect(destinationAttr)
    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    sourceAttr.value = 20
    assert sourceAttr.value == 20
    assert destinationAttr.value == 20


def test_should_connectAttribute_given_extraFlags():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translateY')
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    assert not destinationAttr.locked
    sourceAttr.connect(destinationAttr, force=True, lock=True)
    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    assert destinationAttr.locked


def test_should_connectAttribute_given_arrayAttribute():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('multMatrix', name='destination'))
    sourceAttr = mx.Attribute(source, 'worldMatrix')
    destinationAttr = mx.Attribute(destination, 'matrixIn[0]')
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    sourceAttr.connect(destinationAttr)
    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)


def test_should_disconnectAttribute():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translateY')
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    sourceAttr.connect(destinationAttr)
    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)
    sourceAttr.disconnect(destinationAttr)
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)


def test_should_disconnectAttributeInput():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))

    sourceAttr = mx.Attribute(source, 'translate')
    destinationAttr = mx.Attribute(destination, 'translate')

    sourceAttr.connect(destinationAttr)

    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)

    destinationAttr.disconnectInput()

    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)


def test_should_disconnectAttributeOutput_given_singleConnection():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))

    sourceAttr = mx.Attribute(source, 'translate')
    destinationAttr = mx.Attribute(destination, 'translate')

    sourceAttr.connect(destinationAttr)

    assert cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)

    sourceAttr.disconnectOutput()

    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr.fullName)


def test_should_disconnectAttributeOutput_given_multipleConnections():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination1 = mx.Node(cmds.createNode('transform', name='destination1'))
    destination2 = mx.Node(cmds.createNode('transform', name='destination2'))

    sourceAttr = mx.Attribute(source, 'translate')
    destinationAttr1 = mx.Attribute(destination1, 'translate')
    destinationAttr2 = mx.Attribute(destination2, 'translate')

    sourceAttr.connect(destinationAttr1)
    sourceAttr.connect(destinationAttr2)

    assert cmds.isConnected(sourceAttr.fullName, destinationAttr1.fullName)
    assert cmds.isConnected(sourceAttr.fullName, destinationAttr2.fullName)

    sourceAttr.disconnectOutput()

    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr1.fullName)
    assert not cmds.isConnected(sourceAttr.fullName, destinationAttr2.fullName)


def test_should_getInputConnection_given_attributeWithNoConnections():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translate')

    assert not attr.input()


def test_should_getInputConnection_given_attributeWithConnectionsOnBothSides():
    node = mx.Node(cmds.createNode('transform', name='node'))
    inputNode = mx.Node(cmds.createNode('transform', name='inputNode'))
    outputNode = mx.Node(cmds.createNode('transform', name='outputNode'))

    attr = mx.Attribute(node, 'translate')
    inputAttr = mx.Attribute(inputNode, 'translate')
    outputAttr = mx.Attribute(outputNode, 'translate')

    inputAttr.connect(attr)
    attr.connect(outputAttr)

    inputConnection = attr.input()

    assert isinstance(inputConnection, mx.Node)
    assert inputConnection == inputNode


def test_should_getInputConnection_given_specifiedType():
    node = mx.Node(cmds.createNode('transform', name='node'))
    inputNode = mx.Node(cmds.createNode('multiplyDivide', name='inputNode'))

    attr = mx.Attribute(node, 'translate')
    inputAttr = mx.Attribute(inputNode, 'output')

    inputAttr.connect(attr)
    inputConnection = attr.input(type='multiplyDivide')

    assert isinstance(inputConnection, mx.Node)
    assert inputConnection == inputNode


def test_should_getInputConnection_given_specifiedType_and_noValidConnection():
    node = mx.Node(cmds.createNode('transform', name='node'))
    inputNode = mx.Node(cmds.createNode('transform', name='inputNode'))

    attr = mx.Attribute(node, 'translate')
    inputAttr = mx.Attribute(inputNode, 'translate')

    inputAttr.connect(attr)
    inputConnection = attr.input(type='multiplyDivide')

    assert not inputConnection


def test_should_getInputConnectionAttribute_given_plugs():
    node = mx.Node(cmds.createNode('transform', name='node'))
    inputNode = mx.Node(cmds.createNode('transform', name='inputNode'))

    attr = mx.Attribute(node, 'translate')
    inputAttr = mx.Attribute(inputNode, 'translate')

    inputAttr.connect(attr)
    inputConnection = attr.input(plugs=True)

    assert isinstance(inputConnection, mx.Attribute)
    assert inputConnection.fullName == 'inputNode.translate'


def test_should_getOutputConnections_given_attributeWithNoConnections():
    node = mx.Node(cmds.createNode('transform'))
    outputs = mx.Attribute(node, 'translate').outputs()

    assert not outputs
    assert isinstance(outputs, list)


def test_should_getOutputConnections_given_attributeWithConnectionsOnBothSides():
    node = mx.Node(cmds.createNode('transform', name='node'))
    inputNode = mx.Node(cmds.createNode('transform', name='inputNode'))
    outputNode = mx.Node(cmds.createNode('transform', name='outputNode'))

    attr = mx.Attribute(node, 'translate')
    inputAttr = mx.Attribute(inputNode, 'translate')
    outputAttr = mx.Attribute(outputNode, 'translate')

    inputAttr.connect(attr)
    attr.connect(outputAttr)

    outputs = attr.outputs()

    assert len(outputs) == 1
    assert isinstance(outputs[0], mx.Node)
    assert outputs[0] == outputNode


def test_should_getOutputConnections_given_attributeWithMultipleOutputConnections():
    node = mx.Node(cmds.createNode('transform', name='node'))
    outputNode1 = mx.Node(cmds.createNode('transform', name='outputNode1'))
    outputNode2 = mx.Node(cmds.createNode('transform', name='outputNode2'))

    attr = mx.Attribute(node, 'translate')
    outputAttr1 = mx.Attribute(outputNode1, 'translate')
    outputAttr2 = mx.Attribute(outputNode2, 'translate')

    attr.connect(outputAttr1)
    attr.connect(outputAttr2)

    outputs = attr.outputs()

    assert len(outputs) == 2
    assert isinstance(outputs[0], mx.Node)
    assert isinstance(outputs[1], mx.Node)
    assert outputs[0] == outputNode2
    assert outputs[1] == outputNode1


def test_should_getOutputConnections_given_specifiedType():
    node = mx.Node(cmds.createNode('transform', name='node'))
    outputNode1 = mx.Node(cmds.createNode('transform', name='outputNode1'))
    outputNode2 = mx.Node(cmds.createNode('multiplyDivide', name='outputNode2'))

    attr = mx.Attribute(node, 'translate')
    outputAttr1 = mx.Attribute(outputNode1, 'translate')
    outputAttr2 = mx.Attribute(outputNode2, 'input1')

    attr.connect(outputAttr1)
    attr.connect(outputAttr2)

    outputs = attr.outputs(type='multiplyDivide')

    assert len(outputs) == 1
    assert isinstance(outputs[0], mx.Node)
    assert outputs[0] == outputNode2


def test_should_getOutputConnections_given_specifiedType_and_noValidConnections():
    node = mx.Node(cmds.createNode('transform', name='node'))
    outputNode1 = mx.Node(cmds.createNode('transform', name='outputNode1'))
    outputNode2 = mx.Node(cmds.createNode('transform', name='outputNode2'))

    attr = mx.Attribute(node, 'translate')
    outputAttr1 = mx.Attribute(outputNode1, 'translate')
    outputAttr2 = mx.Attribute(outputNode2, 'translate')

    attr.connect(outputAttr1)
    attr.connect(outputAttr2)

    outputs = attr.outputs(type='multiplyDivide')

    assert not outputs
    assert isinstance(outputs, list)


def test_should_getOutputConnectionsAttributes_given_plugs():
    node = mx.Node(cmds.createNode('transform', name='node'))
    outputNode1 = mx.Node(cmds.createNode('transform', name='outputNode1'))
    outputNode2 = mx.Node(cmds.createNode('transform', name='outputNode2'))

    attr = mx.Attribute(node, 'translate')
    outputAttr1 = mx.Attribute(outputNode1, 'translate')
    outputAttr2 = mx.Attribute(outputNode2, 'translate')

    attr.connect(outputAttr1)
    attr.connect(outputAttr2)

    outputs = attr.outputs(plugs=True)

    assert len(outputs) == 2
    assert isinstance(outputs[0], mx.Attribute)
    assert isinstance(outputs[1], mx.Attribute)
    assert outputs[0].fullName == 'outputNode2.translate'
    assert outputs[1].fullName == 'outputNode1.translate'


def test_should_raiseMayaAttributeError_given_invalidExtraFlag_when_connecting():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translateY')
    with pytest.raises(mx.MayaAttributeError):
        sourceAttr.connect(destinationAttr, invalidExtraFlag=True)


def test_should_raiseMayaAttributeError_given_incompatibleAttributes_when_connecting():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translate')
    with pytest.raises(mx.MayaAttributeError):
        sourceAttr.connect(destinationAttr)


def test_should_raiseMayaAttributeError_given_notConnectedAttributes_when_disconnecting():
    source = mx.Node(cmds.createNode('transform', name='source'))
    destination = mx.Node(cmds.createNode('transform', name='destination'))
    sourceAttr = mx.Attribute(source, 'translateX')
    destinationAttr = mx.Attribute(destination, 'translateY')
    with pytest.raises(mx.MayaAttributeError):
        sourceAttr.disconnect(destinationAttr)
