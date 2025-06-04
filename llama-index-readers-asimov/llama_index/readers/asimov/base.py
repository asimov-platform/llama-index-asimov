# This is free and unencumbered software released into the public domain.

from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document
from typing import List

class AsimovReader(BaseReader):
    """ASIMOV reader."""

    def load_data(self) -> List[Document]:
        return list() # TODO
