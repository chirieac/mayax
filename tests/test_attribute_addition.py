import pytest

from maya import cmds

import mayax as mx


class SomeVector(mx.Vector):
    pass


class SomeMatrix(mx.Matrix):
    pass


def test_should_deleteAttribute():
    node = mx.Node(cmds.createNode('transform', name='testNode'))
    cmds.addAttr(node.name, longName='testAttr')

    assert cmds.attributeQuery('testAttr', node='testNode', exists=True)

    mx.Attribute(node, 'testAttr').delete()

    assert not cmds.attributeQuery('testAttr', node='testNode', exists=True)


# --------------------------------------------------------------------------------------------------


def test_should_addAttribute_given_extraFlags():
    node = mx.Node(cmds.createNode('transform'))
    attr = mx.Attribute(node, 'testAttr', value='blah blah', sn='blah', nn='Nice Blah', k=True)
    assert cmds.getAttr(attr.fullName, type=True) == 'string'
    assert cmds.addAttr(attr.fullName, query=True, longName=True) == 'testAttr'
    assert cmds.addAttr(attr.fullName, query=True, shortName=True) == 'blah'
    assert cmds.addAttr(attr.fullName, query=True, niceName=True) == 'Nice Blah'
    assert cmds.addAttr(attr.fullName, query=True, keyable=True)


def test_should_raiseMayaAttributeError_given_existingAttributeName_when_adding():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        mx.Attribute(node, 'translateX', 0.0)


def test_should_raiseMayaAttributeError_given_existingClassAttributeName_when_adding():
    node = mx.Node(cmds.createNode('transform'))
    node.testAttr = 'test'
    with pytest.raises(mx.MayaAttributeError):
        mx.Attribute(node, 'testAttr', 'test')


def test_should_raiseMayaAttributeError_given_invalidType():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        mx.Attribute(node, 'testAttr', type='__invalidtype__')


def test_should_raiseMayaAttributeError_given_uknownValue_and_noType():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        mx.Attribute(node, 'testAttr', object)


def test_should_raiseMayaAttributeError_given_unknownExtraFlag():
    node = mx.Node(cmds.createNode('transform'))
    with pytest.raises(mx.MayaAttributeError):
        mx.Attribute(node, 'testAttr', 0, unkownFlag=0)


# --------------------------------------------------------------------------------------------------


def test_should_addFloatAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type='float')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'float'


def test_should_addFloatAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type=float)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'float'


def test_should_addFloatAttribute_given_zeroValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', 0.0)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'float'
    assert not cmds.getAttr('{}.testAttr'.format(node.uniqueName))


def test_should_addFloatAttribute_given_nonZeroValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', 20.5)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'float'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName)) == 20.5


# --------------------------------------------------------------------------------------------------


def test_should_addIntAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type='long')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'long'


def test_should_addIntAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type=int)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'long'


def test_should_addIntAttribute_given_zeroValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', 0)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'long'
    assert not cmds.getAttr('{}.testAttr'.format(node.uniqueName))


def test_should_addIntAttribute_given_nonZeroValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', 11)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'long'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName)) == 11


# --------------------------------------------------------------------------------------------------


def test_should_addBoolAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type='bool')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'bool'


def test_should_addBoolAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type=bool)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'bool'


def test_should_addBoolAttribute_given_trueValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', True)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'bool'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName))


def test_should_addBoolAttribute_given_falseValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', False)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'bool'
    assert not cmds.getAttr('{}.testAttr'.format(node.uniqueName))


# --------------------------------------------------------------------------------------------------


def test_should_addStringAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type='string')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'string'


def test_should_addStringAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', type=str)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'string'


def test_should_addStringAttribute_given_emptyValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', '')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'string'
    assert not cmds.getAttr('{}.testAttr'.format(node.uniqueName))


def test_should_addStringAttribute_given_nonEmptyValue():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'testAttr', 'blah blah')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'string'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName)) == 'blah blah'


# --------------------------------------------------------------------------------------------------


def test_should_addVectorAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type='double3')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'double3'


def test_should_addVectorAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type=mx.Vector)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'double3'


def test_should_addVectorAttribute_given_pyTypeSubclass():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type=SomeVector)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'double3'


def test_should_addVectorAttribute_given_zeroValue():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'vectorAttr', mx.Vector(0, 0, 0))
    assert cmds.getAttr('{}.vectorAttr'.format(node.uniqueName), type=True) == 'double3'
    assert cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName), type=True) == 'double'
    assert not cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName))
    assert not cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName))
    assert not cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName))


def test_should_addVectorAttribute_given_nonZeroValue():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'vectorAttr', mx.Vector(10.0, 12, 7.5))
    assert cmds.getAttr('{}.vectorAttr'.format(node.uniqueName), type=True) == 'double3'
    assert cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName)) == 10.0
    assert cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName)) == 12.0
    assert cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName)) == 7.5


def test_should_addVectorAttribute_given_shortName():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'vectorAttr', mx.Vector(10.0, 12, 7.5), shortName='va')
    assert cmds.getAttr('{}.va'.format(node.uniqueName), type=True) == 'double3'
    assert cmds.getAttr('{}.vaX'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vaY'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vaZ'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vaX'.format(node.uniqueName)) == 10.0
    assert cmds.getAttr('{}.vaY'.format(node.uniqueName)) == 12.0
    assert cmds.getAttr('{}.vaZ'.format(node.uniqueName)) == 7.5


def test_should_addVectorAttribute_given_subclassedVector():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'vectorAttr', SomeVector(10.0, 12, 7.5))
    assert cmds.getAttr('{}.vectorAttr'.format(node.uniqueName), type=True) == 'double3'
    assert cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName), type=True) == 'double'
    assert cmds.getAttr('{}.vectorAttrX'.format(node.uniqueName)) == 10.0
    assert cmds.getAttr('{}.vectorAttrY'.format(node.uniqueName)) == 12.0
    assert cmds.getAttr('{}.vectorAttrZ'.format(node.uniqueName)) == 7.5


# --------------------------------------------------------------------------------------------------


def test_should_addMatrixAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type='matrix')
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'


def test_should_addMatrixAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type=mx.Matrix)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'


def test_should_addMatrixAttribute_given_pyTypeSubclass():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', type=SomeMatrix)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'


def test_should_addMatrixAttribute_given_zeroValue():
    mtx = mx.Matrix([
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1)
    ])
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', mtx)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName)) == [
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
    ]


def test_should_addMatrixAttribute_given_nonZeroValue():
    mtx = mx.Matrix([
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (20, 33, 45, 1)
    ])
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', mtx)
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName)) == [
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        20, 33, 45, 1
    ]


def test_should_addMatrixAttribute_given_subclassedMatrix():
    node = mx.Node(cmds.createNode('transform'))
    assert mx.Attribute(node, 'testAttr', SomeMatrix())
    assert cmds.getAttr('{}.testAttr'.format(node.uniqueName), type=True) == 'matrix'


# --------------------------------------------------------------------------------------------------


def test_should_addMessageAttribute_given_type():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'messageAttr', type='message')
    assert cmds.getAttr('{}.messageAttr'.format(node.uniqueName), type=True) == 'message'


def test_should_addMessageAttribute_given_pyType():
    node = mx.Node(cmds.createNode('transform'))
    mx.Attribute(node, 'messageAttr', type=mx.Node)
    assert cmds.getAttr('{}.messageAttr'.format(node.uniqueName), type=True) == 'message'
