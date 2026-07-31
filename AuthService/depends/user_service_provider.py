from fastapi import Depends

from depends.dpns_manager import DependsManager
from infrastructure.uow.sqlalchemy_uow import SQLAlchemyUnitOfWork
from infrastructure.tokens.jwt_t_service import JWTTokenService
from infrastructure.tokens.redis_t_repository import RedisTokenRepository
from infrastructure.users.sqlalchemy_u_repository import SQLAlchemyUserRepository
from use_cases.users.u_service import UserService


async def user_service_provider(depends_manager: DependsManager = Depends()) -> UserService:
    user_repo = SQLAlchemyUserRepository()
    sqlalchemy_uow = SQLAlchemyUnitOfWork(depends_manager.db.session_factory,
                                          user_repo
                                          )
    client = await depends_manager.cache.get_client()
    token_repo = RedisTokenRepository(client=client)
    token_service = JWTTokenService(token_repo=token_repo)
    return UserService(uow=sqlalchemy_uow, user_repo=user_repo, token_service=token_service)