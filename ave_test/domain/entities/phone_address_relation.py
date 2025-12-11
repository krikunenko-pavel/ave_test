from ave_test.domain.value_objects import PhoneVO, AddressVO


class PhoneAddressRelation:
    def __init__(self, phone: PhoneVO, address: AddressVO):
        self.phone = phone
        self.address = address
