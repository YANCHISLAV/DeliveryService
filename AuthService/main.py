from contextlib import asynccontextmanager

from fastapi import FastAPI

from configs.settings import get_settings
from depends.user_service_provider import user_service_provider
from infrastructure.db.session import Database
from infrastructure.redis.client import Redis
from interface_adapters.users.u_dpns import i_user_service
from interface_adapters.users import u_views



@asynccontextmanager
async def lifespan(app: FastAPI):
    db = Database(**get_settings().db.model_dump())
    cache = Redis(**get_settings().cache.model_dump())
    app.state.db = db
    app.state.cache = cache

    yield

    await db.dispose()
    await cache.close()

app = FastAPI(lifespan=lifespan)

app.include_router(u_views.router)

app.dependency_overrides[i_user_service] = user_service_provider