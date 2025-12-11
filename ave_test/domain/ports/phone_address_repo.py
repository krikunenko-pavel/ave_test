

from abc import (ABC, abstractmethod)
from typing import Optional
from ave_test.domain.entities import PhoneAddressRelation
from ave_test.domain.value_objects import PhoneVO

class PhoneAddressRepo(ABC):

    @abstractmethod
    async def get_address_phone(self, phone: PhoneVO) -> Optional[PhoneAddressRelation]:
        raise NotImplementedError()
    

    @abstractmethod
    async def save(self, item: PhoneAddressRelation):
        raise NotImplementedError()
    

    @abstractmethod
    async def delete(self, phone: PhoneVO):
        raise NotImplementedError()
    

    



