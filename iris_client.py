import os
from typing import Iterator, Optional

from authlib.integrations.httpx_client import AsyncOAuth2Client, OAuth2Client
from authlib.oauth2.rfc6749 import OAuth2Token

DEFAULT_BASE_URL = "https://api.iris.dioptra.io"
LOGIN_URL = "/auth/jwt/login"

USERNAME_ENV = "IRIS_USERNAME"
PASSWORD_ENV = "IRIS_PASSWORD"

PAGINATION_DATA_KEY = "results"
PAGINATION_NEXT_KEY = "next"

__version__ = "0.2.1"


class IrisClient(OAuth2Client):
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        fetch_token: bool = True,
        **kwargs,
    ):
        super().__init__(base_url=base_url, **kwargs)
        self.username = username or os.environ.get(USERNAME_ENV)
        self.password = password or os.environ.get(PASSWORD_ENV)
        self.fetch_token_ = fetch_token

    def __enter__(self):
        super().__enter__()
        if self.fetch_token_:
            self.fetch_token()
        return self

    def fetch_token(self, **kwargs) -> OAuth2Token:
        return super().fetch_token(
            LOGIN_URL, username=self.username, password=self.password
        )

    def all(self, url: str, **kwargs) -> Iterator[dict]:
        while url:
            data = self.get(url, **kwargs).json()
            url = data[PAGINATION_NEXT_KEY]
            yield from data[PAGINATION_DATA_KEY]


class AsyncIrisClient(AsyncOAuth2Client):
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        fetch_token: bool = True,
        **kwargs,
    ):
        super().__init__(base_url=base_url, **kwargs)
        self.username = username or os.environ.get(USERNAME_ENV)
        self.password = password or os.environ.get(PASSWORD_ENV)
        self.fetch_token_ = fetch_token

    async def __aenter__(self):
        await super().__aenter__()
        if self.fetch_token_:
            await self.fetch_token()
        return self

    async def fetch_token(self, **kwargs) -> OAuth2Token:
        return await super().fetch_token(
            LOGIN_URL, username=self.username, password=self.password
        )

    async def all(self, url: str, **kwargs) -> Iterator[dict]:
        while url:
            data = (await self.get(url, **kwargs)).json()
            url = data[PAGINATION_NEXT_KEY]
            for obj in data[PAGINATION_DATA_KEY]:
                yield obj
