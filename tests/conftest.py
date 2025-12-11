from httpx import ASGITransport, AsyncClient
import pytest
from fastapi import FastAPI

from ave_test.domain.ports import PhoneAddressRepo
from ave_test.domain.entities import PhoneAddressRelation
from ave_test.domain.value_objects import PhoneVO, AddressVO
from ave_test.app.services import PhoneAddressService
from ave_test.interface.http.controller import PhoneAddressController

class MockPhoneAddressRepo(PhoneAddressRepo):
    def __init__(self):
        self.store: dict[str, str] = {}

    async def save(self, item: PhoneAddressRelation):
        self.store[item.phone.value] = item.address.value

    async def get_address_phone(self, phone: PhoneVO) -> PhoneAddressRelation:
        res = self.store.get(phone.value)
        if not res:
            return res
        return PhoneAddressRelation(PhoneVO(phone), AddressVO(res))

    async def delete(self, phone: PhoneVO):
        self.store.pop(phone.value)


@pytest.fixture(scope="session")
def build_test_app() -> FastAPI:
    repo = MockPhoneAddressRepo()
    service = PhoneAddressService(repo)
    controller = PhoneAddressController(service)
    app = FastAPI()
    yield controller.register_controller(app)


@pytest.fixture(scope="function")
def test_client(build_test_app):
    yield AsyncClient(
        transport=ASGITransport(app=build_test_app), base_url="http://test_app"
    )