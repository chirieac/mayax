import pytest

from maya import cmds
from maya.api import OpenMaya as om

import mayax as mx


def test_should_getFloatValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 20.0, 6.0, node.uniqueName)
    assert isinstance(mx.Attribute(node, 'translateX').value, float)
    assert mx.Attribute(node, 'translateX').value == 15.0
    assert mx.Attribute(node, 'translateY').value == 20.0
    assert mx.Attribute(node, 'translateZ').value == 6.0


def test_should_getIntValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testAttr', attributeType='long')
    cmds.setAttr('{}.testAttr'.format(node.uniqueName), 32)
    attr = mx.Attribute(node, 'testAttr')
    assert isinstance(attr.value, int)
    assert attr.value == 32


def test_should_getBoolValue():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'visibility')
    assert isinstance(attr.value, bool)
    assert attr.value


def test_should_getStringValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testAttr', dataType='string')
    cmds.setAttr('{}.testAttr'.format(node.uniqueName), 'blablah', type='string')
    attr = mx.Attribute(node, 'testAttr')
    assert isinstance(attr.value, mx.STR_TYPE)
    assert attr.value == 'blablah'


def test_should_getVectorValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 20.15, 6.6, node.uniqueName)
    attrValue = mx.Attribute(node, 'translate').value
    assert isinstance(attrValue, mx.Vector)
    assert attrValue.x == 15.0
    assert attrValue.y == 20.15
    assert attrValue.z == 6.6


def test_should_getMatrixValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 20.15, 6.6, node.uniqueName)
    attrValue = mx.Attribute(node, 'worldMatrix').value
    assert isinstance(attrValue, mx.Matrix)
    assert attrValue.getElement(3, 0) == 15
    assert attrValue.getElement(3, 1) == 20.15
    assert attrValue.getElement(3, 2) == 6.6
    assert attrValue.getElement(3, 3) == 1


def test_should_getQuaternionValue():
    node = mx.Node(cmds.createNode('eulerToQuat'))
    cmds.setAttr('{}.inputRotate'.format(node.uniqueName), 15.0, 20.15, 6.6)
    attrValue = mx.Attribute(node, 'outputQuat').value
    assert isinstance(attrValue, mx.Quaternion)
    assert round(attrValue.x, 3) == 0.118
    assert round(attrValue.y, 3) == 0.181
    assert round(attrValue.z, 3) == 0.033
    assert round(attrValue.w, 3) == 0.976


def test_should_getColorValue():
    node = mx.Node(cmds.createNode('ambientLight'))

    cmds.setAttr('{}.color'.format(node.uniqueName), 0.2, 0.35, 0.9)

    attrValue = mx.Attribute(node, 'color').value

    assert isinstance(attrValue, tuple)
    assert attrValue == pytest.approx((0.2, 0.35, 0.9))


def test_should_getValue_given_time():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translateX')

    cmds.setKeyframe(node.uniqueName, attribute='translateX', time=1, value=10)
    cmds.setKeyframe(node.uniqueName, attribute='translateX', time=5, value=50)

    assert attr.value == 10
    assert attr.valueAt(1) == 10
    assert attr.valueAt(50) == 50


# --------------------------------------------------------------------------------------------------


def test_should_setFloatValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.move(15.0, 0.0, 0.0, node.uniqueName)
    attr = mx.Attribute(node, 'translateX')
    assert attr.value == 15.0
    attr.value = 32.45
    assert attr.value == 32.45


def test_should_setIntValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testAttr', attributeType='long')
    cmds.setAttr('{}.testAttr'.format(node.uniqueName), 32)
    attr = mx.Attribute(node, 'testAttr')
    assert attr.value == 32
    attr.value = 999
    assert attr.value == 999


def test_should_setBoolValue():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'visibility')
    assert attr.value
    attr.value = False
    assert not attr.value
    attr.value = True
    assert attr.value


def test_should_setStringValue():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testAttr', dataType='string')
    cmds.setAttr('{}.testAttr'.format(node.uniqueName), 'blablah', type='string')
    attr = mx.Attribute(node, 'testAttr')
    assert attr.value == 'blablah'
    attr.value = 'hello'
    assert attr.value == 'hello'


def test_should_setVectorValue_given_vector():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translate')
    assert not attr.value.x
    assert not attr.value.y
    assert not attr.value.z
    attr.value = mx.Vector(20.0, 13, 7.5)
    assert attr.value.x == 20.0
    assert attr.value.y == 13.0
    assert attr.value.z == 7.5


def test_should_setVectorValue_given_openMayaVector():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translate')
    assert not attr.value.x
    assert not attr.value.y
    assert not attr.value.z
    attr.value = om.MVector(20.0, 13, 7.5)
    assert attr.value.x == 20.0
    assert attr.value.y == 13.0
    assert attr.value.z == 7.5


def test_should_setVectorValue_given_tuple():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translate')
    assert not attr.value.x
    assert not attr.value.y
    assert not attr.value.z
    attr.value = (20.0, 13, 7.5)
    assert attr.value.x == 20.0
    assert attr.value.y == 13.0
    assert attr.value.z == 7.5


def test_should_setVectorValue_given_list():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'translate')
    assert not attr.value.x
    assert not attr.value.y
    assert not attr.value.z
    attr.value = [20.0, 13, 7.5]
    assert attr.value.x == 20.0
    assert attr.value.y == 13.0
    assert attr.value.z == 7.5


def test_should_setMatrixValue_given_matrix():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testMatrix', attributeType='matrix')
    attr = mx.Attribute(node, 'testMatrix')
    assert not attr.value.getElement(3, 0)
    assert not attr.value.getElement(3, 1)
    assert not attr.value.getElement(3, 2)
    assert attr.value.getElement(3, 3) == 1
    attr.value = mx.Matrix([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (20, 33, 45, 1)])
    assert attr.value.getElement(3, 0) == 20
    assert attr.value.getElement(3, 1) == 33
    assert attr.value.getElement(3, 2) == 45
    assert attr.value.getElement(3, 3) == 1


def test_should_setMatrixValue_given_openMayaMatrix():
    node = mx.Node(cmds.createNode('transform'))
    cmds.addAttr(node.uniqueName, longName='testMatrix', attributeType='matrix')
    attr = mx.Attribute(node, 'testMatrix')
    assert not attr.value.getElement(3, 0)
    assert not attr.value.getElement(3, 1)
    assert not attr.value.getElement(3, 2)
    assert attr.value.getElement(3, 3) == 1
    attr.value = om.MMatrix([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (20, 33, 45, 1)])
    assert attr.value.getElement(3, 0) == 20
    assert attr.value.getElement(3, 1) == 33
    assert attr.value.getElement(3, 2) == 45
    assert attr.value.getElement(3, 3) == 1


def test_should_setMatrixValue_given_emptyArrayAttribute_and_matrix():
    node = mx.Node(cmds.createNode('multMatrix'))
    attr = mx.Attribute(node, 'matrixIn[0]')

    assert not attr.value.getElement(3, 0)
    assert not attr.value.getElement(3, 1)
    assert not attr.value.getElement(3, 2)
    assert attr.value.getElement(3, 3) == 1

    attr.value = mx.Matrix([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (20, 33, 45, 1)])

    assert attr.value.getElement(3, 0) == 20
    assert attr.value.getElement(3, 1) == 33
    assert attr.value.getElement(3, 2) == 45
    assert attr.value.getElement(3, 3) == 1


def test_should_setQuaternionValue_given_quaternion():
    node = mx.Node(cmds.createNode('quatToEuler'))
    assert not cmds.getAttr('{}.outputRotateX'.format(node.uniqueName))
    assert not cmds.getAttr('{}.outputRotateY'.format(node.uniqueName))
    assert not cmds.getAttr('{}.outputRotateZ'.format(node.uniqueName))
    mx.Attribute(node, 'inputQuat').value = mx.Quaternion(45, 90, 0, 0)
    assert cmds.getAttr('{}.outputRotateX'.format(node.uniqueName)) == 180
    assert not cmds.getAttr('{}.outputRotateY'.format(node.uniqueName))
    assert round(cmds.getAttr('{}.outputRotateZ'.format(node.uniqueName)), 3) == 126.870


def test_should_setQuaternionValue_given_openMayaQuaternion():
    node = mx.Node(cmds.createNode('quatToEuler'))
    assert not cmds.getAttr('{}.outputRotateX'.format(node.uniqueName))
    assert not cmds.getAttr('{}.outputRotateY'.format(node.uniqueName))
    assert not cmds.getAttr('{}.outputRotateZ'.format(node.uniqueName))
    mx.Attribute(node, 'inputQuat').value = om.MQuaternion(45, 90, 0, 0)
    assert cmds.getAttr('{}.outputRotateX'.format(node.uniqueName)) == 180
    assert not cmds.getAttr('{}.outputRotateY'.format(node.uniqueName))
    assert round(cmds.getAttr('{}.outputRotateZ'.format(node.uniqueName)), 3) == 126.870


def test_should_setColorValue_given_tuple():
    node = mx.Node(cmds.createNode('ambientLight'))

    assert cmds.getAttr('{}.color'.format(node.uniqueName))[0] == (1, 1, 1)

    mx.Attribute(node, 'color').value = (0.2, 0.35, 0.9)

    assert cmds.getAttr('{}.color'.format(node.uniqueName))[0] == pytest.approx((0.2, 0.35, 0.9))
