from abc import ABC, abstractmethod

from domain.entities.user import User


class UserRepoInterface(ABC):

    @abstractmethod
    async def create(self, user)->User:
        pass

    @abstractmethod
    async def get_by_id(self)->User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str)->User|None:
        pass

    @abstractmethod
    async def update(self)->User:
        pass