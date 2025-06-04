# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Chat stores."""

from ._version import __version__, __version_tuple__
from .base import AsimovChatStore

__all__ = [
    'AsimovChatStore',
    '__version__',
    '__version_tuple__',
]
