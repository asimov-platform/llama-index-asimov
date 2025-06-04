# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Index stores."""

from ._version import __version__, __version_tuple__
from .base import AsimovIndexStore

__all__ = [
    'AsimovIndexStore',
    '__version__',
    '__version_tuple__',
]
