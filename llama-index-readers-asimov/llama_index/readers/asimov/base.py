# This is free and unencumbered software released into the public domain.

from __future__ import annotations

import json
import logging
import subprocess
from typing import List, cast

from .errors import AsimovModuleNotFound
from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document
from pyld import jsonld

logger = logging.getLogger(__name__)

JSONLD_CONTEXT = {
    "@version": 1.1,
    "know": "https://know.dev/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


class AsimovReader(BaseReader):
    """
    ASIMOV reader.

    Setup:
        Install ``llama-index-asimov``:

        ```bash
        pip install -U llama-index-asimov
        ```

    Instantiate:
        ```python
        from llama_index.readers.asimov import AsimovReader

        reader = AsimovReader(
            module="serpapi",
            url="https://duckduckgo.com/?q=Isaac+Asimov"
        )
        ```
    """

    def __init__(self, module: str, url: str) -> None:
        self.module = module
        self.url = url

    def load_data(self) -> List[Document]:
        try:
            result = subprocess.run(
                [f"asimov-{self.module}-importer", self.url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            result.check_returncode()
            output = json.loads(result.stdout)
            output = cast(dict, jsonld.flatten(output, JSONLD_CONTEXT))

            docs = []
            for resource in output["@graph"]:
                resource_id = resource["@id"]
                page_content = describe(resource)
                docs.append(Document(text=page_content, id=resource_id, metadata=resource))
            return docs

        except FileNotFoundError as error:
            # logger.exception(error)
            raise AsimovModuleNotFound(self.module) from (error if __debug__ else None)
        except subprocess.CalledProcessError as error:
            # logger.exception(error)
            raise error  # TODO
        except json.decoder.JSONDecodeError as error:
            # logger.exception(error)
            raise error  # TODO
        except jsonld.JsonLdError as error:
            # logger.exception(error)
            raise error  # TODO


def describe(resource: dict) -> str:
    prioritized_keys = ["know:summary", "know:title", "know:name", "know:link"]
    for key in prioritized_keys:
        if key in resource:
            return resource[key]["@value"] if isinstance(resource[key], dict) and "@value" in resource[key] else resource[key]
    return resource["@id"]
