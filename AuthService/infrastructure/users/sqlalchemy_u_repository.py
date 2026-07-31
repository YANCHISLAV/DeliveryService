from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.user import User
from infrastructure.users.u_model import UserModel
from use_cases.users.u_repo_interface import UserRepoInterface


class SQLAlchemyUserRepository(UserRepoInterface):
    def __init__(self, session: AsyncSession | None = None):
        self.session = session

    async def get_by_email(self, email: str)->User|None:
        query = select(UserModel).where(UserModel.email == email)
        query_res = await self.session.execute(query)
        user_model = query_res.scalar()
        if not user_model:
            return None
        return User.model_validate(user_model)

    async def get_by_id(self):
        pass

    async def create(self, user)->User:
        user_model = UserModel(**user.model_dump())
        self.session.add(user_model)
        await self.session.flush()
        await self.session.refresh(user_model)
        return User.model_validate(user_model)

    async def update(self):
        pass