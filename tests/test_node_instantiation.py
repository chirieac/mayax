import pytest

from maya import cmds
from maya.api import OpenMaya as om

import mayax as mx


def test_should_getInstanceFromScene_given_name():
    cmds.createNode('transform')
    assert mx.Node('transform1')


def test_should_getInstanceFromScene_given_node():
    cmds.createNode('transform')
    assert mx.Node(mx.Node('transform1'))


def test_should_getInstanceFromScene_given_mobject():
    cmds.createNode('transform')
    mobject = om.MGlobal.getSelectionListByName('transform1').getDependNode(0)
    assert mx.Node(mobject)


def test_should_raiseMayaNodeError_given_none():
    with pytest.raises(mx.MayaNodeError):
        mx.Node(None)


def test_should_raiseMayaNodeError_given_nonexistentName():
    with pytest.raises(mx.MayaNodeError):
        mx.Node('nonexistentNodeName')
