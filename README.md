# 🕸️ Iris Python Client

[![Tests](https://img.shields.io/github/workflow/status/dioptra-io/iris-client/Tests?logo=github)](https://github.com/dioptra-io/iris-client/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/codecov/c/github/dioptra-io/iris-client?logo=codecov&logoColor=white)](https://app.codecov.io/gh/dioptra-io/iris-client)
[![PyPI](https://img.shields.io/pypi/v/dioptra-iris-client?logo=pypi&logoColor=white)](https://pypi.org/project/dioptra-iris-client/)

Minimal Python client for the [Iris](https://github.com/dioptra-io/iris) API,
built on top of [Authlib](https://github.com/lepture/authlib) and [httpx](https://github.com/encode/httpx).

## Installation

```bash
pip install iris-client
```

## Usage

```python
from iris_client import IrisClient, AsyncIrisClient

# NOTE: If the username and/or the password are not specified,
# they will be retrieved from the `IRIS_USERNAME` and `IRIS_PASSWORD` environment variables.

# Synchronous client
with IrisClient("user@example.org", "password") as client:
    measurements = client.get("/measurements/").json()

# Asynchronous client
async with AsyncIrisClient("user@example.org", "password") as client:
    measurements = (await client.get("/measurements/")).json()

# Helper function to fetch all the results from a paginated endpoint,
# available for both clients:
all_measurements = client.get_all("/measurements/")
```
