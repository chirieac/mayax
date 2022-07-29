"""Maya exceptions."""


class MayaError(Exception):
    """Base class for all Maya exceptions."""


class MayaNodeError(MayaError):
    """Raised by the `Node` class."""


class MayaAttributeError(MayaError, AttributeError):
    """Raised by the `Attribute` class."""
