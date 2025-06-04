# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Embeddings."""

from ._version import __version__, __version_tuple__
from .base import AsimovEmbedding

__all__ = [
    'AsimovEmbedding',
    '__version__',
    '__version_tuple__',
]
