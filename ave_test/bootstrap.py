from fastapi import FastAPI
from redis.asyncio import ConnectionPool
from ave_test.interface.http.controller import PhoneAddressController
from ave_test.app.services import PhoneAddressService
from ave_test.adapters import RedisRepo
from ave_test.config import AppConfig


def build_app() -> FastAPI:
    config = AppConfig()
    pool = ConnectionPool.from_url(str(config.redis_dsn))
    repo = RedisRepo(pool)
    service = PhoneAddressService(repo)
    controller = PhoneAddressController(service)
    app = FastAPI(title="PhoneAddressService")
    return controller.register_controller(app)
