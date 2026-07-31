from abc import ABC, abstractmethod
from typing import Any


class UnitOfWorkInterface(ABC):

    users: Any

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return await self.rollback()
        else:
            return await self.commit()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()