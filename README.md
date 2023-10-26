# 🕸️ Iris Python Client

[![Tests](https://img.shields.io/github/actions/workflow/status/dioptra-io/iris-client/tests.yml?logo=github)](https://github.com/dioptra-io/iris-client/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/codecov/c/github/dioptra-io/iris-client?logo=codecov&logoColor=white)](https://app.codecov.io/gh/dioptra-io/iris-client)
[![PyPI](https://img.shields.io/pypi/v/dioptra-iris-client?logo=pypi&logoColor=white)](https://pypi.org/project/dioptra-iris-client/)

Minimalist Python client for the [Iris](https://github.com/dioptra-io/iris) API,
built on top of [Authlib](https://github.com/lepture/authlib) and [httpx](https://github.com/encode/httpx).

## Installation

```bash
pip install dioptra-iris-client
```

## Usage

```python
from iris_client import IrisClient, AsyncIrisClient

base_url = "https://api.iris.dioptra.io"
username = "user@example.org"
password = "password"

# Synchronous client
with IrisClient(base_url, username, password) as client:
    measurements = client.get("/measurements/").json()

# Asynchronous client
async with AsyncIrisClient(base_url, username, password) as client:
    measurements = (await client.get("/measurements/")).json()

# Helper function to fetch all the results from a paginated endpoint,
# available for both clients:
all_measurements = client.all("/measurements/")
```


### Credential provider chain

The Iris client looks for credentials in a way similar to the [AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html):

1. If one of `base_url`, `username` or `password` is specified, these values will be used.
2. If none of the previous values are specified, and one of `IRIS_BASE_URL`, `IRIS_USERNAME` or `IRIS_PASSWORD`
   environment variables are present, these values will be used.
3. If none of the previous values are specified, and the file `~/.config/iris/credentials.json` exists,
   the fields `base_url`, `username` and `password` will be used.
