"""Wrap a maya node."""

from __future__ import absolute_import

import math

from maya import cmds
from maya.api import OpenMaya as om

from .exceptions import MayaNodeError, MayaAttributeError
from .math import Vector, Matrix, Quaternion
from .strtype import STR_TYPE


class Node(object):
    """Wrap a Maya node.

    Parameters
    ----------
    node : str or Node or MObject
        The name (or instance) of an existing node.

    Raises
    ------
    MayaNodeError
        When something went wrong.
    """

    def __new__(cls, node):
        """Create an object instance based on the provided `node`."""
        pyClass = cls
        mobject = None
        nodeFn = None
        nameFn = None
        uniqueNameFn = None

        if node is None:
            raise MayaNodeError('Invalid node name.')

        if isinstance(node, om.MObject):
            mobject = node
        elif isinstance(node, Node):
            node = node.uniqueName

        if not mobject:
            try:
                mobject = om.MGlobal.getSelectionListByName(node).getDependNode(0)
            except RuntimeError:
                raise MayaNodeError(
                    'Maya node "{}" does not exist (or is not unique).'.format(node)
                )

        if mobject.hasFn(om.MFn.kDagNode):
            nodeFn = om.MFnDagNode(mobject)
            nameFn = nodeFn.name
            uniqueNameFn = nodeFn.partialPathName
        else:
            nodeFn = om.MFnDependencyNode(mobject)
            nameFn = nodeFn.name
            uniqueNameFn = nameFn

        pyClass = cls.__findPyClass(nodeFn)

        if not pyClass or not issubclass(pyClass, cls):
            raise MayaNodeError('The provided node is not of type "{}".'.format(cls.__name__))

        obj = object.__new__(pyClass)

        obj.__dict__['apiObject'] = mobject
        obj.__dict__['apiObjectHandle'] = om.MObjectHandle(mobject)
        obj.__dict__['_Node__nameFn'] = nameFn
        obj.__dict__['_Node__uniqueNameFn'] = uniqueNameFn

        return obj

    @classmethod
    def __findPyClass(cls, nodeFn):
        nodeType = nodeFn.typeName

        # 1: Search for exact node wrap.
        if cls.__name__.lower() == nodeType.lower():
            return cls

        # 2: Search for specialized node.
        if nodeFn.type() == om.MFn.kDagNode:
            return DagNode
        if cls is Node:
            return cls

        return None

    def __getitem__(self, name):
        return Attribute(self, name)

    def __getattr__(self, name):
        return self[name].value

    def __setattr__(self, name, value):
        isPyAttribute = (
            hasattr(self.__class__, name) or name in self.__dict__ or not self.hasAttr(name)
        )

        if isPyAttribute:
            super(Node, self).__setattr__(name, value)
        else:
            self[name].value = value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.apiObjectHandle == other.apiObjectHandle

        if isinstance(other, STR_TYPE):
            try:
                return self.apiObjectHandle == Node(other).apiObjectHandle
            except MayaNodeError:
                return False

        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Node):
            return self.apiObjectHandle != other.apiObjectHandle

        if isinstance(other, STR_TYPE):
            try:
                return self.apiObjectHandle != Node(other).apiObjectHandle
            except MayaNodeError:
                return True

        return NotImplemented

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self.uniqueName)

    def __str__(self):
        return self.uniqueName

    @property
    def exists(self):
        """Check if the node still exists."""
        return self.apiObjectHandle.isValid()

    @property
    def name(self):
        """Get the node's name."""
        if self.exists:
            return self.__nameFn()

        raise MayaNodeError('Node is no longer valid.')

    @name.setter
    def name(self, name):
        self.rename(name)

    def rename(self, name, **kwargs):
        """Rename the node.

        Use `kwargs` to pass extra flags used by ``maya.cmds.rename``.

        For simple cases use the `name` property setter.
        """
        cmds.rename(self.uniqueName, name, **kwargs)

    @property
    def uniqueName(self):
        """Get the node's unique name.

        For extra rename functionality use `rename()`.
        """
        if self.exists:
            return self.__uniqueNameFn()

        raise MayaNodeError('Node is no longer valid.')

    @property
    def type(self):
        """str: The node's type."""
        return cmds.nodeType(self.uniqueName)

    def delete(self):
        """Delete the node."""
        cmds.delete(self.uniqueName)

    def duplicate(self, **kwargs):
        """Duplicate the node.

        Use `kwargs` to pass extra flags used by ``maya.cmds.duplicate``.
        """
        return Node(cmds.duplicate(self.uniqueName, **kwargs)[0])

    def select(self, **kwargs):
        """Select the node.

        Use `kwargs` to pass extra flags used by ``maya.cmds.select``.
        """
        cmds.select(self.uniqueName, **kwargs)

    def addAttr(self, name, value=None, type=None, **kwargs):  # pylint: disable=W0622
        """Add an attribute to the node.

        See `Attribute` class for more info.

        Returns
        -------
        Attribute
            The attribute instance.

        Raises
        ------
        MayaNodeError
            If insufficient arguments are provided.
        MayaAttributeError
            If the attribute couldn't be added.
        """
        createAttr = value is not None or type or 'dataType' in kwargs or 'attributeType' in kwargs
        if not createAttr:
            raise MayaNodeError('Value or type must be provided.')

        return Attribute(self, name, value, type, **kwargs)

    def deleteAttr(self, name):
        """Delete the provided attribute."""
        Attribute(self, name).delete()

    def hasAttr(self, name):
        """Check if the node has an attribute."""
        try:
            Attribute(self, name)
            return True
        except MayaAttributeError:
            return False


# --------------------------------------------------------------------------------------------------
# Attribute
# --------------------------------------------------------------------------------------------------


_PY_ATTRIBUTE_TYPES = {
    str: 'string',
    float: 'float',
    int: 'long',
    bool: 'bool',
    Vector: 'double3',
    Matrix: 'matrix',
    Node: 'message',
}
_ATTRIBUTE_TYPES = [
    'bool',
    'long',
    'short',
    'byte',
    'char',
    'enum',
    'float',
    'double',
    'doubleAngle',
    'doubleLinear',
    'compound',
    'message',
    'time',
    'matrix',
    'fltMatrix',
    'reflectance',
    'spectrum',
    'float2',
    'float3',
    'double2',
    'double3',
    'long2',
    'long3',
    'short2',
    'short3',
]
_DATA_TYPES = [
    'string',
    'stringArray',
    'matrix',
    'reflectanceRGB',
    'spectrumRGB',
    'float2',
    'float3',
    'double2',
    'double3',
    'long2',
    'long3',
    'short2',
    'short3',
    'doubleArray',
    'floatArray',
    'Int32Array',
    'vectorArray',
    'pointArray',
    'nurbsCurve',
    'nurbsSurface',
    'mesh',
    'lattice',
]


class Attribute(object):
    """Wrap a Maya attribute.

    Parameters
    ----------
    node : str or `Node`
        The node that holds the attribute.
    name : str
        The attribute's long name.
    value : any
        The value of the attribute. Used only when adding a new attribute.
    type : string
        The attribute type (see ``maya.cmds.addAttr``). Used only when adding a new attribute.
    kwargs :
        Extra flags used by ``maya.cmds.addAttr``.

    Raises
    ------
    MayaAttributeError
        When something went wrong.
    """

    def __init__(self, node, name=None, value=None, type=None, **kwargs):  # pylint: disable=W0622
        if isinstance(node, STR_TYPE):
            if name:
                node = Node(node)
            else:
                attrParts = node.split('.', 1)

                if len(attrParts) == 2:
                    node = Node(attrParts[0])
                    name = attrParts[1]
                else:
                    raise MayaAttributeError(
                        'Attribute name could not be retrieved from "{}".'.format(node)
                    )

        create = value is not None or type or 'dataType' in kwargs or 'attributeType' in kwargs

        if create:
            Attribute.__addAttr(node, name, value, type, kwargs)
        else:
            try:
                cmds.getAttr('{}.{}'.format(node.uniqueName, name.split('[')[0]), size=True)
            except ValueError:
                raise MayaAttributeError(
                    'Attribute "{}.{}" does not exist.'.format(node.uniqueName, name)
                )

        self.__node = node
        self.__name = name

        if create and value is not None:
            self.value = value

    @staticmethod
    def __addAttr(node, name, value, attrType, kwargs):
        if name in node.__dict__:
            raise MayaAttributeError(
                'Node object already has an attribute named "{}".'.format(name)
            )

        kwargs['longName'] = name

        Attribute.__inferType(value, attrType, kwargs)

        try:
            cmds.addAttr(node.uniqueName, **kwargs)

            if 'attributeType' in kwargs and kwargs['attributeType'] == 'double3':
                childKwargs = {'parent': name}

                childKwargs['longName'] = name + 'X'
                if 'shortName' in kwargs:
                    childKwargs['shortName'] = kwargs['shortName'] + 'X'
                cmds.addAttr(node.uniqueName, **childKwargs)

                childKwargs['longName'] = name + 'Y'
                if 'shortName' in kwargs:
                    childKwargs['shortName'] = kwargs['shortName'] + 'Y'
                cmds.addAttr(node.uniqueName, **childKwargs)

                childKwargs['longName'] = name + 'Z'
                if 'shortName' in kwargs:
                    childKwargs['shortName'] = kwargs['shortName'] + 'Z'
                cmds.addAttr(node.uniqueName, **childKwargs)
        except (RuntimeError, TypeError) as e:
            raise MayaAttributeError(e)

    @staticmethod
    def __inferType(value, attrType, kwargs):
        if not attrType and 'dataType' not in kwargs and 'attributeType' not in kwargs:
            attrType = type(value)

        if isinstance(attrType, type):
            if issubclass(attrType, Node):
                attrType = Node
            elif issubclass(attrType, Vector):
                attrType = Vector
            elif issubclass(attrType, Matrix):
                attrType = Matrix

            if attrType in _PY_ATTRIBUTE_TYPES:
                attrType = _PY_ATTRIBUTE_TYPES[attrType]
            else:
                raise MayaAttributeError('Type could not be inferred from "{}".'.format(attrType))

        if attrType in _ATTRIBUTE_TYPES:
            kwargs['attributeType'] = attrType
        elif attrType in _DATA_TYPES:
            kwargs['dataType'] = attrType
        else:
            raise MayaAttributeError('Invalid type "{}".'.format(attrType))

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self.fullName)

    def __str__(self):
        return self.fullName

    @property
    def name(self):
        """str: The attribute's name."""
        return self.__name

    @property
    def fullName(self):
        """str: The attribute's name with the node's name in it."""
        return '{}.{}'.format(self.__node.uniqueName, self.__name)

    @property
    def node(self):
        """`Node`: The attribute's node."""
        return self.__node

    @property
    def type(self):
        """str: The attribute's type."""
        return cmds.getAttr(self.fullName, type=True)

    @property
    def value(self):
        """any: The attribute's value."""
        return self.valueAt(None)

    @value.setter
    def value(self, value):
        if self.type == 'message':
            if value:
                if isinstance(value, STR_TYPE):
                    value = Node(value)
                value['message'].connect(self, force=True)
            elif self.value:
                self.value['message'].disconnect(self)
        else:
            args = (value,)
            kwargs = {}

            if isinstance(value, STR_TYPE):
                kwargs['type'] = 'string'
            elif isinstance(value, (om.MVector, tuple, list)) and self.type == 'float3':
                kwargs['type'] = 'float3'
                args = tuple(value)
            elif isinstance(value, (om.MVector, tuple, list)) and self.type == 'double3':
                kwargs['type'] = 'double3'
                args = tuple(value)
            elif isinstance(value, om.MMatrix):
                kwargs['type'] = 'matrix'
                args = tuple(value)
            elif isinstance(value, om.MQuaternion):
                args = tuple(value)

            cmds.setAttr(self.fullName, *args, **kwargs)

    def valueAt(self, time):
        """Get the attribute's value."""
        cmdFlags = {}

        if time is not None:
            cmdFlags['time'] = time

        if self.type == 'message':
            nodeName = cmds.connectionInfo(self.fullName, sourceFromDestination=True)

            if nodeName:
                return Node(nodeName.split('.')[0])

            return None

        value = cmds.getAttr(self.fullName, **cmdFlags)

        if self.type == 'float3':
            value = value[0]
        elif self.type == 'double3':
            value = Vector(value[0])
        elif self.type == 'matrix':
            if value is None:  # to fix Maya 2019
                value = Matrix.kIdentity
            else:
                value = Matrix(value)
        elif self.type == 'TdataCompound':
            isQuat = (
                len(value)
                and len(value[0]) == 4
                and cmds.attributeQuery(
                    self.__name + 'W',
                    node=self.__node.uniqueName,
                    exists=True,
                )
            )
            if isQuat:
                value = Quaternion(value[0])  # pylint: disable=redefined-variable-type

        return value

    @property
    def locked(self):
        """bool: The attribute's lock state."""
        return cmds.getAttr(self.fullName, lock=True)

    @locked.setter
    def locked(self, value):
        cmds.setAttr(self.fullName, lock=value)

    @property
    def keyable(self):
        """bool: The attribute's keyable state."""
        return cmds.getAttr(self.fullName, keyable=True)

    @keyable.setter
    def keyable(self, value):
        cmds.setAttr(self.fullName, keyable=value)

    @property
    def channelBox(self):
        """bool: The attribute's channelBox state."""
        return cmds.getAttr(self.fullName, channelBox=True)

    @channelBox.setter
    def channelBox(self, value):
        cmds.setAttr(self.fullName, channelBox=value)

    def connect(self, attr, **kwargs):
        """Connect the attribute to another.

        Parameters
        ----------
        attr : Attribute
            The destination attribute receiving the connection.
        kwargs :
            Extra flags used by ``maya.cmds.connectAttr``.

        Raises
        ------
        MayaAttributeError
            If the connection was not successful.
        """
        try:
            cmds.connectAttr(self.fullName, attr.fullName, **kwargs)
        except (RuntimeError, TypeError) as e:
            raise MayaAttributeError(e)

    def delete(self):
        """Delete the attribute."""
        cmds.deleteAttr(self.fullName)

    def disconnect(self, attr, **kwargs):
        """Disconnect the attribute from another.

        Parameters
        ----------
        attr : Attribute
            The destination attribute to disconnect from.
        kwargs :
            Extra flags used by ``maya.cmds.disconnectAttr``.

        Raises
        ------
        MayaAttributeError
            If the disconnection was not successful.
        """
        try:
            cmds.disconnectAttr(self.fullName, attr.fullName, **kwargs)
        except (RuntimeError, TypeError) as e:
            raise MayaAttributeError(e)

    def disconnectInput(self):
        """Disconnect the attribute's input."""
        inputAttr = self.input(plugs=True)

        if inputAttr:
            inputAttr.disconnect(self)

    def disconnectOutput(self):
        """Disconnect the attribute's output."""
        outputs = self.outputs(plugs=True)

        for attr in outputs:
            self.disconnect(attr)

    def input(self, **kwargs):
        """Get the attribute's input connection.

        Use `kwargs` to pass extra flags used by ``maya.cmds.listConnections``.
        """
        kwargs['destination'] = False
        connections = cmds.listConnections(self.fullName, **kwargs)

        if connections:
            if 'plugs' in kwargs:
                return Attribute(connections[0])

            return Node(connections[0])

        return None

    def outputs(self, **kwargs):
        """Get the attribute's output connections.

        Use `kwargs` to pass extra flags used by ``maya.cmds.listConnections``.
        """
        kwargs['source'] = False
        connections = cmds.listConnections(self.fullName, **kwargs)

        if connections:
            if 'plugs' in kwargs:
                return [Attribute(attrFullName) for attrFullName in connections]

            return [Node(nodeName) for nodeName in connections]

        return []


# --------------------------------------------------------------------------------------------------
# Specialized Nodes
# --------------------------------------------------------------------------------------------------


class DagNode(Node):
    """Maintain data related to Maya's Directed Acyclic Graph (DAG)."""

    @property
    def pathName(self):
        """Return the full path from the root of the dag to this object."""
        if not self.exists:
            raise MayaNodeError('Node is no longer valid.')

        return om.MFnDagNode(self.apiObject).fullPathName()

    @property
    def parent(self):
        """`Node`: Get/set the node's parent."""
        try:
            return Node(cmds.listRelatives(self.uniqueName, parent=True, path=True)[0])
        except TypeError:
            return None

    @parent.setter
    def parent(self, value):
        self.setParent(value)

    def setParent(self, value, **kwargs):
        """Set the node's parent.

        Use `kwargs` to pass extra flags used by ``maya.cmds.parent``.

        For simple cases use the `parent` property setter.
        """
        if value:
            if isinstance(value, Node):
                value = value.uniqueName
            cmds.parent(self.uniqueName, value, **kwargs)
        elif self.parent:
            cmds.parent(self.uniqueName, world=True)

    @property
    def children(self):
        """list: Get the node's children."""
        children = cmds.listRelatives(self.uniqueName, children=True, path=True)

        if children:
            return [Node(child) for child in children]

        return []

    @property
    def descendents(self):
        """list: Get the node's descendents."""
        descendents = cmds.listRelatives(self.uniqueName, allDescendents=True, path=True)

        if descendents:
            return [Node(descendent) for descendent in descendents]

        return []

    @property
    def shapes(self):
        """list: Get the node's shapes."""
        shapes = cmds.listRelatives(self.uniqueName, shapes=True, path=True)

        if shapes:
            return [Node(shape) for shape in shapes]

        return []

    def findChildren(self, name):
        """Find children by name."""
        children = cmds.ls('{}|{}'.format(self.pathName, name))

        return [Node(child) for child in children]

    @property
    def worldPosition(self):
        """`Vector`: Return the node's world position."""
        return Vector(cmds.xform(self.uniqueName, query=True, translation=True, worldSpace=True))

    @worldPosition.setter
    def worldPosition(self, value):
        cmds.xform(self.uniqueName, worldSpace=True, translation=value)

    @property
    def worldRotation(self):
        """`Vector`: Return the node's world rotation."""
        return Vector(cmds.xform(self.uniqueName, query=True, rotation=True, worldSpace=True))

    @worldRotation.setter
    def worldRotation(self, value):
        cmds.xform(self.uniqueName, worldSpace=True, rotation=value)

    @property
    def worldScale(self):
        """`Vector`: Return the node's world scale."""
        return Vector(cmds.xform(self.uniqueName, query=True, scale=True, worldSpace=True))

    @worldScale.setter
    def worldScale(self, value):
        scale = self.scale
        worldMatrix = self.worldMatrix

        transformationMatrix = om.MTransformationMatrix(worldMatrix)
        transformationMatrix.setScale(value, om.MSpace.kTransform)

        scaleRatio = om.MTransformationMatrix(
            transformationMatrix.asMatrix() * worldMatrix.inverse()
        ).scale(om.MSpace.kTransform)

        cmds.xform(
            self.uniqueName,
            scale=(
                scale.x * scaleRatio[0],
                scale.y * scaleRatio[1],
                scale.z * scaleRatio[2],
            ),
        )

    @property
    def worldMatrix(self):
        """`Matrix`: Return the node's world matrix."""
        return Matrix(cmds.xform(self.uniqueName, query=True, matrix=True, worldSpace=True))

    @worldMatrix.setter
    def worldMatrix(self, value):
        cmds.xform(self.uniqueName, matrix=value, worldSpace=True)

    def worldPositionAt(self, time):
        """Get the world position at specified time."""
        transformationMatrix = om.MTransformationMatrix(self['worldMatrix'].valueAt(time))

        return Vector(transformationMatrix.translation(om.MSpace.kWorld))

    def worldRotationAt(self, time):
        """Get the world rotation at specified time."""
        transformationMatrix = om.MTransformationMatrix(self['worldMatrix'].valueAt(time))
        rotation = transformationMatrix.rotation()

        return Vector(
            math.degrees(rotation.x),
            math.degrees(rotation.y),
            math.degrees(rotation.z),
        )

    def worldScaleAt(self, time):
        """Get the world scale at specified time."""
        transformationMatrix = om.MTransformationMatrix(self['worldMatrix'].valueAt(time))

        return Vector(transformationMatrix.scale(om.MSpace.kWorld))

    def freezeTransform(self, **kwargs):
        """Make the current transformations be the zero position.

        Use `kwargs` to pass extra flags used by ``maya.cmds.makeIdentity``.
        """
        kwargs['apply'] = True
        cmds.makeIdentity(self.uniqueName, **kwargs)

    def resetTransform(self, **kwargs):
        """Reset transformations back to zero (return to first or last "frozen" position).

        Use `kwargs` to pass extra flags used by ``maya.cmds.makeIdentity``.
        """
        kwargs['apply'] = False
        cmds.makeIdentity(self.uniqueName, **kwargs)
