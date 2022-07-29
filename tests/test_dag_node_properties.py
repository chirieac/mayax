from maya import cmds

import mayax as mx


def test_should_getParent():
    cmds.createNode('unknownDag', name='dagNode')
    assert mx.DagNode('dagNode').parent.uniqueName == 'transform1'


def test_should_getUniqueParent():
    cmds.createNode('transform', name='root1')
    cmds.createNode('transform', name='controls', parent='root1')
    cmds.createNode('transform', name='arm_ctrl', parent='root1|controls')

    cmds.createNode('transform', name='root2')
    cmds.createNode('transform', name='controls', parent='root2')
    cmds.createNode('transform', name='arm_ctrl', parent='root2|controls')

    assert mx.DagNode('root1|controls|arm_ctrl').parent.uniqueName == 'root1|controls'


def test_should_getNoParent_if_notChild():
    cmds.createNode('unknownDag', name='dagNode')
    assert not mx.DagNode('transform1').parent


def test_should_setParent_given_name():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child')
    assert not mx.DagNode('child').parent
    mx.DagNode('child').parent = 'parent'
    assert mx.DagNode('child').parent.uniqueName == 'parent'


def test_should_setParent_given_node():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child')
    assert not mx.DagNode('child').parent
    mx.DagNode('child').parent = mx.Node('parent')
    assert mx.DagNode('child').parent.uniqueName == 'parent'


def test_should_setWorldParent_given_none():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    assert mx.DagNode('child').parent.uniqueName == 'parent'
    mx.DagNode('child').parent = None
    assert not mx.DagNode('child').parent


def test_should_setWorldParent_given_unparentedNode():
    cmds.createNode('transform', name='child')
    node = mx.DagNode('child')
    node.parent = None
    assert not node.parent


def test_should_reparentShape():
    cmds.createNode('transform', name='newCube')
    cmds.polyCube()
    assert mx.Node('pCubeShape1').parent.uniqueName == 'pCube1'
    mx.DagNode('pCubeShape1').setParent('newCube', shape=True, relative=True)
    assert mx.Node('pCubeShape1').parent.uniqueName == 'newCube'


def test_should_getChildren_given_oneChild():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    assert len(mx.DagNode('parent').children) == 1
    assert mx.DagNode('parent').children[0].uniqueName == 'child'


def test_should_getChildren_given_twoChildren():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child1', parent='parent')
    cmds.createNode('transform', name='child2', parent='parent')
    assert len(mx.DagNode('parent').children) == 2
    assert mx.DagNode('parent').children[0].uniqueName == 'child1'
    assert mx.DagNode('parent').children[1].uniqueName == 'child2'


def test_should_getChildren_given_identicalChildNameUnderDifferentParent():
    cmds.createNode('transform', name='parent1')
    cmds.createNode('transform', name='child', parent='parent1')
    cmds.createNode('transform', name='parent2')
    cmds.createNode('transform', name='child', parent='parent2')
    assert len(mx.DagNode('parent1').children) == 1
    assert mx.DagNode('parent1').children[0].uniqueName == 'parent1|child'


def test_should_getNoChildren_given_emptyParent():
    cmds.createNode('transform', name='parent')
    assert isinstance(mx.DagNode('parent').children, list)
    assert not mx.DagNode('parent').children


def test_should_getDescendents_given_jointsChain():
    cmds.joint(name='root')
    cmds.joint(name='knee')
    cmds.joint(name='ankle')

    children = mx.DagNode('root').children
    descendents = mx.DagNode('root').descendents

    assert len(children) == 1
    assert children[0].uniqueName == 'knee'

    assert len(descendents) == 2
    assert descendents[0].uniqueName == 'ankle'
    assert descendents[1].uniqueName == 'knee'


def test_should_getNoDescendents_given_emptyParent():
    cmds.createNode('transform', name='parent')
    descendents = mx.DagNode('parent').descendents

    assert not descendents
    assert isinstance(descendents, list)


def test_should_getShapes_given_nodeWithOneShape():
    cmds.polyCube(name='cube')

    shapes = mx.DagNode('cube').shapes

    assert len(shapes) == 1
    assert shapes[0].name == 'cubeShape'


def test_should_getShapes_given_nodeWithTwoShapes():
    cmds.polyCube(name='cube')
    cmds.polySphere(name='sphere')

    mx.DagNode('sphereShape').setParent('cube', shape=True, relative=True)

    shapes = mx.DagNode('cube').shapes

    assert len(shapes) == 2
    assert shapes[0].name == 'cubeShape'
    assert shapes[1].name == 'sphereShape'


def test_should_getNoShapes_given_emptyNode():
    cmds.createNode('transform', name='parent')

    shapes = mx.DagNode('parent').shapes

    assert isinstance(shapes, list)
    assert not shapes


def test_should_findChildren_given_specificName():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child1', parent='parent')
    cmds.createNode('transform', name='child2', parent='parent')

    foundChildren = mx.DagNode('parent').findChildren('child1')

    assert len(foundChildren) == 1
    assert foundChildren[0].uniqueName == 'child1'


def test_should_findChildren_given_wildcardName():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child1', parent='parent')
    cmds.createNode('transform', name='child2', parent='parent')
    cmds.createNode('transform', name='extraChild', parent='parent')

    foundChildren = mx.DagNode('parent').findChildren('child*')

    assert len(foundChildren) == 2
    assert foundChildren[0].uniqueName == 'child1'
    assert foundChildren[1].uniqueName == 'child2'


def test_should_findNoChildren_given_inexistentName():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child1', parent='parent')
    cmds.createNode('transform', name='child2', parent='parent')

    foundChildren = mx.DagNode('parent').findChildren('iDoNotExist')

    assert not foundChildren
    assert isinstance(foundChildren, list)


# --------------------------------------------------------------------------------------------------


def test_should_getWorldPosition():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.move(10, 20, 45, 'parent')
    cmds.move(1, 2, 15, 'child', relative=True)

    worldPosition = mx.DagNode('child').worldPosition

    assert isinstance(worldPosition, mx.Vector)
    assert worldPosition == mx.Vector(11, 22, 60)


def test_should_getWorldPosition_given_time():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.move(10, 20, 45, 'parent')
    cmds.move(1, 2, 15, 'child', relative=True)

    node = mx.DagNode('child')

    cmds.setKeyframe(node.uniqueName)
    cmds.setKeyframe(node.uniqueName, attribute='translateX', time=5, value=55)

    worldPosition = node.worldPosition
    futureWorldPosition = node.worldPositionAt(5)

    assert isinstance(futureWorldPosition, mx.Vector)
    assert worldPosition == mx.Vector(11, 22, 60)
    assert futureWorldPosition == mx.Vector(65, 22, 60)


def test_should_setWorldPosition():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.move(10, 20, 45, 'parent')

    node = mx.DagNode('child')
    node.worldPosition = mx.Vector(11, 22, 60)

    assert node.translate == mx.Vector(1, 2, 15)
    assert node.worldPosition == mx.Vector(11, 22, 60)


def test_should_setWorldPosition_given_locatorTransform():
    locator = cmds.spaceLocator(name='child')[0]
    cmds.createNode('transform', name='parent')
    cmds.parent(locator, 'parent')

    cmds.move(10, 20, 45, 'parent')

    node = mx.DagNode('child')
    node.worldPosition = mx.Vector(11, 22, 60)

    assert node.translate == mx.Vector(1, 2, 15)
    assert node.worldPosition == mx.Vector(11, 22, 60)


def test_should_getWorldRotation():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.rotate(10, 20, 45, 'parent')
    cmds.rotate(1, 2, 15, 'child', relative=True)

    node = mx.DagNode('child')

    assert isinstance(node.worldRotation, mx.Vector)
    assert node.worldRotation.isEquivalent(mx.Vector(16.05, 18.67, 60.97), 0.1)


def test_should_getWorldRotation_given_time():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.rotate(10, 20, 45, 'parent')
    cmds.rotate(1, 2, 15, 'child', relative=True)

    node = mx.DagNode('child')

    cmds.setKeyframe(node.uniqueName)
    cmds.setKeyframe(node.uniqueName, attribute='rotateX', time=5, value=55)

    worldRotation = node.worldRotation
    futureWorldRotation = node.worldRotationAt(5)

    assert isinstance(futureWorldRotation, mx.Vector)
    assert worldRotation.isEquivalent(mx.Vector(16.05, 18.67, 60.97), 0.1)
    assert futureWorldRotation.isEquivalent(mx.Vector(70.05, 18.67, 60.97), 0.1)


def test_should_setWorldRotation():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.rotate(10, 20, 45, 'parent')

    node = mx.DagNode('child')
    node.worldRotation = mx.Vector(16, 18, 60)

    assert node.rotate.isEquivalent(mx.Vector(1.22, 1.10, 14.27), 0.1)
    assert node.worldRotation.isEquivalent(mx.Vector(16, 18, 60))


def test_should_getWorldScale():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.scale(4, 1, 1.5, 'parent')
    cmds.scale(1, 2, 15, 'child', relative=True)

    worldScale = mx.DagNode('child').worldScale

    assert isinstance(worldScale, mx.Vector)
    assert worldScale == mx.Vector(4, 2, 22.5)


def test_should_getWorldScale_given_time():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.scale(4, 1, 1.5, 'parent')
    cmds.scale(1, 2, 15, 'child', relative=True)

    node = mx.DagNode('child')

    cmds.setKeyframe(node.uniqueName)
    cmds.setKeyframe(node.uniqueName, attribute='scaleX', time=5, value=3)

    worldScale = node.worldScale
    futureWorldScale = node.worldScaleAt(5)

    assert isinstance(futureWorldScale, mx.Vector)
    assert worldScale == mx.Vector(4, 2, 22.5)
    assert futureWorldScale == mx.Vector(12, 2, 22.5)


def test_should_setWorldScale_given_noParent():
    cmds.createNode('transform', name='obj')

    node = mx.DagNode('obj')
    node.worldScale = mx.Vector(4, 5, 1)

    assert node.scale.isEquivalent(mx.Vector(4, 5, 1), 0.001)
    assert node.worldScale.isEquivalent(mx.Vector(4, 5, 1), 0.001)


def test_should_setWorldScale_given_scaledParent():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.scale(2, 1, 3, 'parent')

    node = mx.DagNode('child')
    node.worldScale = mx.Vector(4, 5, 1)

    assert node.scale.isEquivalent(mx.Vector(2, 5, 0.333), 0.001)
    assert node.worldScale.isEquivalent(mx.Vector(4, 5, 1), 0.001)


def test_should_setWorldScale_given_scaledParentJoint_and_unitChildScale():
    cmds.joint(position=mx.Vector(-2, 0, 0), name='parentJoint')
    cmds.joint(position=mx.Vector(4, 0, 0), name='childJoint')

    cmds.scale(2, 1, 3, 'parentJoint')

    node = mx.DagNode('childJoint')
    node.worldScale = mx.Vector(1, 1, 1)

    assert node.scale.isEquivalent(mx.Vector(1, 1, 1), 0.001)
    assert node.worldScale.isEquivalent(mx.Vector(1, 1, 1), 0.001)


def test_should_getWorldMatrix():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')

    cmds.move(2, 4, 3, 'parent')
    cmds.rotate(-11, 12, 30, 'parent')
    cmds.scale(2, 2, 2, 'parent')

    cmds.move(5, 6, 13, 'child')
    cmds.rotate(11, 45, 0, 'child')
    cmds.scale(2, 2, 2, 'child')

    worldMatrix = mx.DagNode('child').worldMatrix

    assert isinstance(worldMatrix, mx.Matrix)
    assert list(worldMatrix) == cmds.getAttr('child.worldMatrix')


def test_should_setWorldMatrix():
    cmds.createNode('transform', name='parent')
    cmds.createNode('transform', name='child', parent='parent')
    cmds.createNode('transform', name='target')

    cmds.move(2, 4, 3, 'parent')
    cmds.rotate(-11, 12, 30, 'parent')
    cmds.scale(2, 2, 2, 'parent')

    cmds.move(5, 6, 13, 'target')
    cmds.rotate(11, 45, 0, 'target')
    cmds.scale(2, 2, 2, 'target')

    child = mx.DagNode('child')
    target = mx.DagNode('target')

    child.worldMatrix = target.worldMatrix

    assert child.worldPosition.isEquivalent(mx.Vector(5, 6, 13), 0.001)
    assert child.worldRotation.isEquivalent(mx.Vector(11, 45, 0), 0.001)
    assert child.worldScale.isEquivalent(mx.Vector(2, 2, 2), 0.001)
