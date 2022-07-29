import pytest

from maya import cmds

import mayax as mx


def test_should_getInstanceFromScene():
    cmds.createNode('unknownDag', name='dagNode')
    assert isinstance(mx.DagNode('dagNode'), mx.DagNode)


def test_should_getInstanceFromScene_when_usingNodeClass():
    cmds.createNode('unknownDag', name='dagNode')
    assert isinstance(mx.Node('dagNode'), mx.DagNode)


def test_should_raiseMayaNodeError_given_none():
    with pytest.raises(mx.MayaNodeError):
        mx.DagNode(None)


def test_should_raiseMayaNodeError_given_dgNode():
    with pytest.raises(mx.MayaNodeError):
        mx.DagNode('lambert1')
