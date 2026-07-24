from abc import ABC, abstractmethod

from domain.entities.restaurant import Restaurant


class RestaurantRepoInterface(ABC):


    @abstractmethod
    async def get_by_address(self, r_inp)->Restaurant:
        pass

    @abstractmethod
    async def create(self, r_inp)->Restaurant:
        pass
