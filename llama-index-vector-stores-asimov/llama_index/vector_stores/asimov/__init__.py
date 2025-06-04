# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex"""

from ._version import __version__, __version_tuple__
from .base import AsimovVectorStore

__all__ = [
    'AsimovVectorStore',
    '__version__',
    '__version_tuple__',
]
