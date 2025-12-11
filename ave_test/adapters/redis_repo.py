

from typing import AsyncGenerator
import redis.asyncio as redis
from ave_test.domain.ports import PhoneAddressRepo
from ave_test.domain.entities import PhoneAddressRelation
from ave_test.domain.value_objects import (PhoneVO, AddressVO,)

class RedisRepo(PhoneAddressRepo):

    def __init__(self, client: redis.ConnectionPool):
        self._client = client
        super().__init__()
    
    
    async def client(self):
        return await redis.Redis.from_pool(self._client)

    async def save(self, item: PhoneAddressRelation):
        client = await self.client()
        await client.set(item.phone.value, item.address.value)
        await client.aclose()

    async def get_address_phone(self, phone: PhoneVO) -> PhoneAddressRelation:
        client = await self.client()
        result = await client.get(phone.value)
        await client.aclose()
        if not result:
            return result
        return PhoneAddressRelation(
            phone=phone,
            address=AddressVO(result)
        )
    
    async def delete(self, phone: PhoneVO):
        client = await self.client()
        await client.delete(phone.value)
    

    
    