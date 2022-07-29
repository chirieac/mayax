# Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
    - [Node Properties](#node-properties)
    - [Node methods](#node-methods)
    - [Attribute Properties](#attribute-properties)
    - [Attribute methods](#attribute-methods)


# Introduction

**MayaX** provides useful functionality to interact with **Maya**, mainly making it easier to work with **nodes** in an **object-oriented** way. It supports *Maya 2019* and up (maybe lower than 2019 too, but it wasn't tested).

```python
import mayax as mx

# retrieve object from scene
torus = mx.Node('pTorus1')

# create new node
cube = mx.cmd.polyCube()[0]

# connect nodes
torus['worldMatrix'].connect(cube['offsetParentMatrix'])

# set attribute value
cube.translate = mx.Vector(0, 5, 0)

# set attribute's properties
cube['translate'].locked = True

# add node reference as attribute
cube.addAttr('parentDriver', torus)

# retrieve node reference
cube.parentDriver.worldPosition = mx.Vector(2, 5, 5)
```


# Installation

**a.** Drag `install.py` script into Maya's viewport.

**b.** Manually create the `mayax.mod` module file and put it in your favorite location:

    + MayaX 1.0.0 <mayax path>
    scripts: src

**c.** Copy `src/mayax` into your project.


# Usage

- `import mayax as mx`

- Use `mx.Node('objectFromScene')` to retrieve an existing node using its name.

- Use `mx.cmd.*` namespace to call the Maya's commands in order to have them accept and return instances of `mx.Node`.

- Retrieve and set the values for the node's attributes's as you would for regular Python objects (`node.attributeName = value`).

- Do operations on the attributes themselves by accessing them using the notation `node['attributeName']`.

- Add attributes using [node.addAttr()](#add-attr) method.


# API

## Node Properties

- `exists`: Check if the node still exists.

- `name`: Get/set the node's name.

- `uniqueName`: Get the node's unique name.

- `type`: Get the node's type.

- `pathName`: Get the full path from the root of the dag to this object.

- `parent`: Get/set the node's parent.

- `children`: Get the node's children.

- `descendents`: Get the node's descendents.

- `shapes`: Get the node's shapes.

- `worldPosition`: Get/set the node's world position.

- `worldRotation`: Get/set the node's world rotation.

- `worldScale`: Get/set the node's world scale.

- `worldMatrix`: Get/set the node's world matrix.


## Node Methods

- `rename(name, **kwargs)`: Rename the node.

    Use `kwargs` to pass extra flags used by `maya.cmds.rename`.
    For simple cases use the `name` property *setter*.

- `delete()`: Delete the node.

- `duplicate(**kwargs)`: Duplicate the node.

    Use `kwargs` to pass extra flags used by `maya.cmds.duplicate`.

- `select(**kwargs)`: Select the node.

    Use `kwargs` to pass extra flags used by `maya.cmds.select`.

<a id="add-attr"></a>
- `addAttr(name, value=None, type=None, **kwargs)`: Add an attribute to the node.

    Use `kwargs` to pass extra flags used by `maya.cmds.addAttr`.

    ```python
    # add an attribute by inferring its type from the value
    node.addAttr('name', 25.5)
    node.addAttr('name', nodeInstance)

    # add an attribute by providing the type
    node.addAttr('name', type='float')
    node.addAttr('name', nodeInstance, type='message')

    # add an attribute by providing a Python's type
    node.addAttr('name', type=float)
    node.addAttr('name', type=mx.Node)
    node.addAttr('name', type=mx.Vector)
    ```

- `deleteAttr(name)`: Delete the provided attribute.

- `hasAttr(name)`: Check if the node has an attribute.

- `setParent(value, **kwargs)`: Set the node's parent.

    Use `kwargs` to pass extra flags used by `maya.cmds.parent`.
    For simple cases use the `parent` property *setter*.

- `findChildren(name)`: Find children by name.

- `worldPositionAt(time)`: Get the world position at specified time.

- `worldRotationAt(time)`: Get the world rotation at specified time.

- `worldScaleAt(time)`: Get the world scale at specified time.

- `freezeTransform(**kwargs)`: Make the current transformations be the zero position.

    Use `kwargs` to pass extra flags used by `maya.cmds.makeIdentity`.

- `resetTransform(**kwargs)`: Reset transformations back to zero (return to first or last "frozen" position).

    Use `kwargs` to pass extra flags used by `maya.cmds.makeIdentity`.


## Attribute Properties

- `name`: Get the attribute's name.

- `fullName`: Get the attribute's name with the node's name in it.

- `node`: Get the attribute's node.

- `type`: Get the attribute's type.

- `value`: Get/set the attribute's value.

- `locked`: Get/set the attribute's lock state.

- `keyable`: Get/set the attribute's keyable state.

- `channelBox`: Get/set the attribute's channelBox state.

## Attribute Methods

- `valueAt(time)`: Get the attribute's value at the specified time.

- `delete()`: Delete the attribute.

- `connect(attr, **kwargs)`: Connect the attribute to another.

    Use `kwargs` to pass extra flags used by `maya.cmds.connectAttr`.

- `disconnect(attr, **kwargs)`: Disconnect the attribute from another.

    Use `kwargs` to pass extra flags used by `maya.cmds.disconnectAttr`.

- `disconnectInput()`: Disconnect the attribute's input.

- `disconnectOutput()`: Disconnect the attribute's output.

- `input(**kwargs)`: Get the attribute's input connection.

     Use `kwargs` to pass extra flags used by `maya.cmds.listConnections`.

- `outputs(**kwargs)`: Get the attribute's output connections.

     Use `kwargs` to pass extra flags used by `maya.cmds.listConnections`.
