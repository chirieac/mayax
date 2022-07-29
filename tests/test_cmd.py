import mayax as mx


def test_should_returnNode():
    locator = mx.cmd.group(empty=True)

    assert locator.uniqueName == 'null1'


def test_should_returnNodeList():
    locator = mx.cmd.spaceLocator()

    assert len(locator) == 1
    assert locator[0].uniqueName == 'locator1'


def test_should_returnOriginalList():
    locator = mx.cmd.spaceLocator()
    result = mx.cmd.xform(locator, query=True, translation=True, worldSpace=True)

    assert result == [0, 0, 0]


def test_should_passNodeAsArgument():
    child1 = mx.cmd.createNode('transform')
    child2 = mx.cmd.createNode('transform')
    mx.cmd.group(child1, child2)

    assert child1.parent.uniqueName == 'group1'
    assert child2.parent.uniqueName == 'group1'


def test_should_passNodeAsArgument_given_nodeWithNonUniqueName():
    parent1 = mx.cmd.createNode('transform', name='parent1')
    child1 = mx.cmd.createNode('transform', name='child', parent=parent1)

    parent2 = mx.cmd.createNode('transform', name='parent2')
    mx.cmd.createNode('transform', name='child', parent=parent2)

    mx.cmd.select(child1)

    assert mx.cmd.ls(selection=True)[0].uniqueName == 'parent1|child'


def test_should_passNodeAsKeywordArgument():
    parent = mx.cmd.createNode('transform')
    child = mx.cmd.createNode('transform', parent=parent)

    assert child.parent.uniqueName == 'transform1'


def test_should_passNodeAsKeywordArgument_given_nodeWithNonUniqueName():
    parent1 = mx.cmd.createNode('transform', name='parent1')
    child1 = mx.cmd.createNode('transform', name='child', parent=parent1)

    parent2 = mx.cmd.createNode('transform', name='parent2')
    mx.cmd.createNode('transform', name='child', parent=parent2)

    child = mx.cmd.createNode('transform', parent=child1)

    assert child.parent.uniqueName == 'parent1|child'


def test_should_passNodeListAsKeywordArgument():
    obj1 = mx.cmd.createNode('transform')
    obj2 = mx.cmd.createNode('transform')

    container = mx.cmd.container(addNode=[obj1, obj2])
    containerNodes = mx.cmd.container(container, query=True, nodeList=True)

    assert containerNodes[0].uniqueName == 'transform1'
    assert containerNodes[1].uniqueName == 'transform2'


def test_should_passNodeListAsKeywordArgument_given_nodeWithNonUniqueName():
    parent1 = mx.cmd.createNode('transform', name='parent1')
    child1 = mx.cmd.createNode('transform', name='child', parent=parent1)

    parent2 = mx.cmd.createNode('transform', name='parent2')
    child2 = mx.cmd.createNode('transform', name='child', parent=parent2)

    container = mx.cmd.container(addNode=[child1, child2])
    containerNodes = mx.cmd.container(container, query=True, nodeList=True)

    assert containerNodes[0].uniqueName == 'parent1|child'
    assert containerNodes[1].uniqueName == 'parent2|child'


def test_should_returnAttribute():
    root = mx.cmd.createNode('transform', name='root')
    leaf = mx.cmd.createNode('transform', name='leaf')

    leaf.addAttr('root', root)

    connectionInfo = mx.cmd.connectionInfo('root.message', getExactSource=True)

    assert isinstance(connectionInfo, mx.Attribute)
    assert connectionInfo.fullName == 'root.message'


def test_should_returnAttributeList():
    root = mx.cmd.createNode('transform', name='root')
    leaf1 = mx.cmd.createNode('transform', name='leaf1')
    leaf2 = mx.cmd.createNode('transform', name='leaf2')

    leaf1.addAttr('root', root)
    leaf2.addAttr('root', root)

    connectedAttributes = mx.cmd.listConnections('root.message', plugs=True)

    assert len(connectedAttributes) == 2
    assert isinstance(connectedAttributes[0], mx.Attribute)
    assert isinstance(connectedAttributes[1], mx.Attribute)
    assert connectedAttributes[0].fullName == 'leaf2.root'
    assert connectedAttributes[1].fullName == 'leaf1.root'


def test_should_passAttributeAsArgument():
    root = mx.cmd.createNode('transform', name='root')
    leaf = mx.cmd.createNode('transform', name='leaf')

    leaf.addAttr('root', root)

    connections = mx.cmd.listConnections(mx.Attribute(root, 'message'))

    assert len(connections) == 1
    assert isinstance(connections[0], mx.Node)
    assert connections[0] == leaf
