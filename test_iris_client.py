from iris_client import AsyncIrisClient, IrisClient


def test_client():
    with IrisClient() as client:
        list(client.get_all("/agents/"))


async def test_async_client():
    async with AsyncIrisClient() as client:
        async for _ in client.get_all("/agents/"):
            pass
