from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from ave_test.app.services import PhoneAddressService
from .dto import (
    CreatePhoneAddressRequest,
    UpdateAddressRequest,
    AddressResponse,
)
from ave_test.domain import errors


class PhoneAddressController:
    def __init__(self, service: PhoneAddressService):
        self.service = service
        self.router = APIRouter()

        self.router.add_api_route("/", self.create_address, methods=["POST"])
        self.router.add_api_route("/{phone}", self.get_address, methods=["GET"])
        self.router.add_api_route("/{phone}", self.update_address, methods=["PATCH"])
        self.router.add_api_route("/{phone}", self.delete_address, methods=["DELETE"])

    async def create_address(self, data: CreatePhoneAddressRequest) -> JSONResponse:
        await self.service.create_phone_address(data.phone, data.address)
        return JSONResponse(content={"status": "ok"}, status_code=201)

    async def get_address(self, phone: str) -> AddressResponse:
        res = await self.service.get_phone_address(phone)
        return AddressResponse(address=res.address.value)

    async def update_address(self, phone: str, address: UpdateAddressRequest):
        await self.service.update_phone_address(phone, address.address)
        return JSONResponse(content={"status": "ok"})

    async def delete_address(self, phone: str) -> JSONResponse:
        await self.service.delete_phone_address(phone)
        return JSONResponse(content={"status": "ok"}, status_code=204)

    def register_controller(self, app: FastAPI) -> FastAPI:
        app.include_router(self.router)
        return self.__register_exceptions(app)

    def __register_exceptions(self, app: FastAPI) -> FastAPI:

        @app.exception_handler(errors.AlreadyExistsError)
        async def handle_already_exist(
            _: Request, exc: errors.AlreadyExistsError
        ) -> JSONResponse:
            return JSONResponse(content={"error": exc.reason}, status_code=409)

        @app.exception_handler(errors.NotFoundError)
        async def handle_not_found(
            _: Request, exc: errors.NotFoundError
        ) -> JSONResponse:
            return JSONResponse(content={"error": exc.reason}, status_code=404)

        return app
