"""Add a compatible string type for Python 2 and 3."""

# pylint: disable=invalid-name

try:
    STR_TYPE = basestring
except NameError:
    STR_TYPE = str
