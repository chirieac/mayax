"""Wrap a Maya attribute."""

# pylint: disable=cyclic-import

from maya import cmds
from maya.api import OpenMaya as om

from .exceptions import MayaAttributeError
from .node import Node
from .math import Vector, Matrix, Quaternion
from .strtype import STR_TYPE


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
