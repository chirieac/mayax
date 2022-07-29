from maya import cmds

import mayax as mx


def test_should_freezeTransformations():
    node = mx.Node(cmds.createNode('transform'))
    node.translate = mx.Vector(15.0, 20.0, 6.0)
    node.rotate = mx.Vector(90, 20, 0)
    node.scale = mx.Vector(1, 2, 3)

    assert node.translate == mx.Vector(15.0, 20.0, 6.0)
    assert node.rotate == mx.Vector(90, 20, 0)
    assert node.scale == mx.Vector(1, 2, 3)

    node.freezeTransform()

    assert node.translate == mx.Vector(0, 0, 0)
    assert node.rotate == mx.Vector(0, 0, 0)
    assert node.scale == mx.Vector(1, 1, 1)


def test_should_freezeTransformations_and_preserve():
    node = mx.Node(cmds.polyCube()[0])
    cmds.group(node.uniqueName)
    node.translate = mx.Vector(15.0, 20.0, 6.0)

    assert node.translate == mx.Vector(15.0, 20.0, 6.0)
    assert node.rotatePivot == mx.Vector(0, 0, 0)

    node.freezeTransform()

    assert node.translate == mx.Vector(0, 0, 0)
    assert node.rotatePivot == mx.Vector(15.0, 20.0, 6.0)


def test_should_freezeOnlyTranslation():
    node = mx.Node(cmds.createNode('transform'))
    node.translate = mx.Vector(15.0, 20.0, 6.0)
    node.rotate = mx.Vector(90, 20, 0)

    assert node.translate == mx.Vector(15.0, 20.0, 6.0)

    node.freezeTransform(translate=True)

    assert node.translate == mx.Vector(0, 0, 0)
    assert node.rotate == mx.Vector(90, 20, 0)


def test_should_resetTransformations():
    node = mx.Node(cmds.createNode('transform'))
    node.translate = mx.Vector(15.0, 20.0, 6.0)
    node.rotate = mx.Vector(90, 20, 0)
    node.scale = mx.Vector(1, 2, 3)

    assert node.translate == mx.Vector(15.0, 20.0, 6.0)
    assert node.rotate == mx.Vector(90, 20, 0)
    assert node.scale == mx.Vector(1, 2, 3)

    node.resetTransform()

    assert node.translate == mx.Vector(0, 0, 0)
    assert node.rotate == mx.Vector(0, 0, 0)
    assert node.scale == mx.Vector(1, 1, 1)
    assert node.rotatePivot == mx.Vector(0, 0, 0)


def test_should_resetOnlyRotation():
    node = mx.Node(cmds.createNode('transform'))
    node.translate = mx.Vector(15.0, 20.0, 6.0)
    node.rotate = mx.Vector(90, 20, 0)

    assert node.rotate == mx.Vector(90, 20, 0)

    node.resetTransform(rotate=True)

    assert node.translate == mx.Vector(15.0, 20.0, 6.0)
    assert node.rotate == mx.Vector(0, 0, 0)
