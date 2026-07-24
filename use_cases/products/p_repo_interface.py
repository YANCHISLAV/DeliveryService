from domain.entities.product import Product
from abc import ABC, abstractmethod


class ProductRepoInterface(ABC):

    @abstractmethod
    async def get_by_id(self, p_id: int)->Product:
        pass

    @abstractmethod
    async def get_by_filters(self, p_filters)->Product:
        pass

    @abstractmethod
    async def get_by_restaurant_id_and_name(self, product)->Product:
        pass

    @abstractmethod
    async def create(self, product)->Product:
        pass
