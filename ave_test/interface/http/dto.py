
from pydantic import BaseModel


class CreatePhoneAddressRequest(BaseModel):
    phone: str
    address: str


class UpdateAddressRequest(BaseModel):
    address: str


class AddressResponse(BaseModel):
    address: str