# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Agents."""

from ._version import __version__, __version_tuple__
from .base import AsimovAgent

__all__ = [
    'AsimovAgent',
    '__version__',
    '__version_tuple__',
]
