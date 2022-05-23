from iris_client import AsyncIrisClient, IrisClient


def test_client():
    with IrisClient() as client:
        client.all("/agents")


async def test_async_client():
    async with AsyncIrisClient() as client:
        await client.all("/agents")
