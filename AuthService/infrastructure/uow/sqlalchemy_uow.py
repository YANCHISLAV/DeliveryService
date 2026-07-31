from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from use_cases.uow.uow_interface import UnitOfWorkInterface


class SQLAlchemyUnitOfWork(UnitOfWorkInterface):

    def __init__(self, session_factory: async_sessionmaker[AsyncSession], *session_objects):
        self.session_factory = session_factory
        self.session: AsyncSession | None = None
        self.session_objects = list(session_objects)


    async def __aenter__(self):
        self.session = self.session_factory()
        for obj in self.session_objects:
            obj.session = self.session
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super().__aexit__(exc_type, exc_val, exc_tb)
        if self.session:
            await self.session.close()

    async def rollback(self):
        if self.session:
            await self.session.rollback()

    async def commit(self):
        if self.session:
            await self.session.commit()