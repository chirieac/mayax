"""Useful math classes and functions."""

import maya.api.OpenMaya as om


class Vector(om.MVector):
    """3D vector with double-precision coordinates.

    See ``maya.api.OpenMaya.MVector`` for more info.
    """


class Matrix(om.MMatrix):
    """4x4 matrix with double-precision elements.

    See ``maya.api.OpenMaya.MMatrix`` for more info.
    """


class Quaternion(om.MQuaternion):
    """Quaternion math.

    See ``maya.api.OpenMaya.MQuaternion`` for more info.
    """


class EulerRotation(om.MEulerRotation):
    """Euler rotation math.

    See ``maya.api.OpenMaya.MEulerRotation`` for more info.
    """
