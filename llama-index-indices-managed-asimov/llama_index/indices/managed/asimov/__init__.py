# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Managed indexes (indices)."""

from ._version import __version__, __version_tuple__
from .base import AsimovManagedIndex

__all__ = [
    'AsimovManagedIndex',
    '__version__',
    '__version_tuple__',
]
