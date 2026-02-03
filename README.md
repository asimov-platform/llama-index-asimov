# llama-index-asimov

[![License](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![Compatibility](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fasimov-platform%2Fllama-index-asimov%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml)](https://pypi.python.org/pypi/llama-index-asimov)
[![Package](https://img.shields.io/pypi/v/llama-index-asimov.svg)](https://pypi.python.org/pypi/llama-index-asimov)

## 📦 Packages

This repository currently provides:

| Package | Description | PyPI |
|---------|-------------|------|
| `llama-index-readers-asimov` | Reader module that runs ASIMOV importers via subprocess | [📦 PyPI](https://pypi.org/project/llama-index-readers-asimov/) |

## 🛠️ Prerequisites

- [Python] 3.10+
- [ASIMOV] [modules] available in the [`PATH`] and/or `$HOME/.asimov/libexec`

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

## 📚 Reference

[llama-index-asimov.readthedocs.io](https://llama-index-asimov.readthedocs.io)

## 👨‍💻 Development

```bash
git clone https://github.com/asimov-platform/langchain-asimov.git
```

[![Share on X](https://img.shields.io/badge/share%20on-x-03A9F4?logo=x)](https://x.com/intent/post?url=https://github.com/asimov-platform/llama-index-asimov&text=llama-index-asimov)
[![Share on Reddit](https://img.shields.io/badge/share%20on-reddit-red?logo=reddit)](https://reddit.com/submit?url=https://github.com/asimov-platform/llama-index-asimov&title=llama-index-asimov)
[![Share on Hacker News](https://img.shields.io/badge/share%20on-hn-orange?logo=ycombinator)](https://news.ycombinator.com/submitlink?u=https://github.com/asimov-platform/llama-index-asimov&t=llama-index-asimov)
[![Share on Facebook](https://img.shields.io/badge/share%20on-fb-1976D2?logo=facebook)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/asimov-platform/llama-index-asimov)
[![Share on LinkedIn](https://img.shields.io/badge/share%20on-linkedin-3949AB?logo=linkedin)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/asimov-platform/llama-index-asimov)

[ASIMOV]: https://github.com/asimov-platform
[LlamaIndex]: https://github.com/run-llama/llama_index
[`PATH`]: https://en.wikipedia.org/wiki/PATH_(variable)
[Python]: https://python.org
[modules]: https://github.com/asimov-modules

[Apify module]: https://github.com/asimov-modules/asimov-apify-module
[Bright Data module]: https://github.com/asimov-modules/asimov-brightdata-module
[SerpApi module]: https://github.com/asimov-modules/asimov-serpapi-module
