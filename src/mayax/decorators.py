"""Decorators."""

import functools

from maya import cmds


def undoable(func):
    """Allow an entire function/method to be undoed."""

    @functools.wraps(func)
    def funcWrapper(*args, **kwargs):
        try:
            cmds.undoInfo(openChunk=True, chunkName=func.__name__)
            return func(*args, **kwargs)
        finally:
            cmds.undoInfo(closeChunk=True, chunkName=func.__name__)

    return funcWrapper
