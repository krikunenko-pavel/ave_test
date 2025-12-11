import pytest


@pytest.mark.asyncio
async def test_create_phone_address(test_client):

    async with test_client as client:
        res = await client.post("/", json={"address": "test_address",
    "phone": "+79000000000"})
        assert res.status_code == 201
        res = await client.post(
            "/", json={"address": "test_address", "phone": "+79000000000"}
        )
        assert res.status_code == 409


@pytest.mark.asyncio
async def test_get_phone_address(test_client):
    async with test_client as client:
        res = await client.get("/+79000000000")
        assert res.status_code == 200
        res = await client.get("/+79000000001")
        assert res.status_code == 404

@pytest.mark.asyncio
async def test_update_phone_address(test_client):
    async with test_client as client:
        res = await client.patch("/+79000000000", json={
            "address": "new_address"
        })
        assert res.status_code == 200
        res = await client.get("/+79000000000")
        assert res.status_code == 200
        assert res.json()["address"] == "new_address"

@pytest.mark.asyncio
async def test_delete_phone_address(test_client):
    async with test_client as client:
        res = await client.delete("/+79000000000")
        assert res.status_code == 204

        res = await client.delete("/8000000000")
        assert res.status_code == 404
