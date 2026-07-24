from abc import ABC, abstractmethod
from domain.entities.order import Order


class OrderRepoInterface(ABC):

    @abstractmethod
    async def get_by_user_id(self, user_id: int)->Order:
        pass

    @abstractmethod
    async def create(self, order)->Order:
        pass