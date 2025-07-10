# llama-index-readers-asimov

[![License](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![Compatibility](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fasimov-platform%2Fllama-index-asimov%2Frefs%2Fheads%2Fmaster%2Fllama-index-readers-asimov%2Fpyproject.toml)](https://pypi.python.org/pypi/llama-index-readers-asimov)
[![Package](https://img.shields.io/pypi/v/llama-index-readers-asimov.svg)](https://pypi.python.org/pypi/llama-index-readers-asimov)

A [LlamaIndex] reader that integrates with the [ASIMOV] platform by invoking external importer modules through subprocess execution.

## 🛠️ Prerequisites

- [Python] 3.9+
- [ASIMOV] [modules] available in the [`PATH`]

## ⬇️ Installation

### Installation from PyPI

```bash
pip install -U llama-index-readers-asimov
```

## 👉 Examples

### DuckDuckGo Results via SerpAPI

```python
from llama_index.readers.asimov import AsimovReader

reader = AsimovReader(
    module="serpapi",
    url="https://duckduckgo.com/?q=LangChain+roadmap"
)

for result in reader.load_data():
    print(result)
```

> [!TIP]
> On your host, make sure that `asimov-serpapi-importer` can be found in your
> `PATH` and that you've defined the `SERPAPI_KEY` environment variable:
>
> ```bash
> export SERPAPI_KEY="..."
> ```

### X (Twitter) Profile via Bright Data

Use e.g. the [Bright Data module] to fetch a public X profile:

```python
from llama_index.readers.asimov import AsimovReader

reader = AsimovReader(
    module="brightdata",
    url="https://x.com/llama_index"
)

for result in reader.load_data():
    print(result)
```

> [!TIP]
> On your host, make sure that `asimov-brightdata-importer` can be found in your
> `PATH` and that you've defined the `BRIGHTDATA_API_KEY` environment variable:
>
> ```bash
> export BRIGHTDATA_API_KEY="..."
> ```

### X (Twitter) Followers via Apify

Use e.g. the [Apify module] to fetch the followers/followees for an X profile:

```python
from llama_index.readers.asimov import AsimovReader

reader = AsimovReader(
    module="apify",
    url="https://x.com/llama_index/followers"
)

for result in reader.load_data():
    print(result)
```

> [!TIP]
> On your host, make sure that `asimov-apify-importer` can be found in your
> `PATH` and that you've defined the `APIFY_TOKEN` environment variable:
>
> ```bash
> export APIFY_TOKEN="..."
> ```

[ASIMOV]: https://github.com/asimov-platform
[LlamaIndex]: https://github.com/run-llama/llama_index
[`PATH`]: https://en.wikipedia.org/wiki/PATH_(variable)
[Python]: https://python.org
[modules]: https://github.com/asimov-modules

[Apify module]: https://github.com/asimov-modules/asimov-apify-module
[Bright Data module]: https://github.com/asimov-modules/asimov-brightdata-module
[SerpApi module]: https://github.com/asimov-modules/asimov-serpapi-module
