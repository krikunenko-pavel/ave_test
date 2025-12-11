from typing import Optional

from ave_test.domain.ports import PhoneAddressRepo
from ave_test.domain.entities import PhoneAddressRelation
from ave_test.domain.value_objects import PhoneVO, AddressVO
from ave_test.domain import errors


class PhoneAddressService:
    def __init__(self, repo: PhoneAddressRepo):
        self.repo = repo
    async def create_phone_address(
        self, phone: str, address: str
    ) -> Optional[PhoneAddressRelation]:
        phone_relation = PhoneAddressRelation(
            phone=PhoneVO(phone), address=AddressVO(address)
        )
        if await self.repo.get_address_phone(phone_relation.phone):
            raise errors.AlreadyExistsError(phone)
        await self.repo.save(phone_relation)

    async def update_phone_address(self, phone: str, address: str):
        if not await self.repo.get_address_phone(PhoneVO(phone)):
            raise errors.NotFoundError(phone)
        item = PhoneAddressRelation(PhoneVO(phone), AddressVO(address))
        await self.repo.save(item)

    async def delete_phone_address(self, phone: str):
        if not await self.repo.get_address_phone(PhoneVO(phone)):
            raise errors.NotFoundError(phone)
        await self.repo.delete(PhoneVO(phone))

    async def get_phone_address(self, phone: str)-> Optional[PhoneAddressRelation]:
        res =await self.repo.get_address_phone(PhoneVO(phone))
        if not res:
            raise errors.NotFoundError(phone)
        return res


