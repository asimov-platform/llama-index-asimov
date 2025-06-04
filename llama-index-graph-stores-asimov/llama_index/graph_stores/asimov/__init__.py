# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex"""

from ._version import __version__, __version_tuple__
from .base import AsimovGraphStore

__all__ = [
    'AsimovGraphStore',
    '__version__',
    '__version_tuple__',
]
