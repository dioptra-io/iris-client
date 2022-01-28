from iris_client import AsyncIrisClient, IrisClient


def test_client():
    with IrisClient() as client:
        res = client.get("/users/me")
        assert res.status_code == 200


async def test_async_client():
    async with AsyncIrisClient() as client:
        res = await client.get("/users/me")
        assert res.status_code == 200
