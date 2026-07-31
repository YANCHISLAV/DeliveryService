from abc import ABC, abstractmethod


class TokenServiceInterface(ABC):

    @abstractmethod
    async def create(self, user_id: int) -> dict:
        pass

    @abstractmethod
    async def update(self, user_id: int)->dict:
        pass

    async def delete(self, user_id: int)->None:
        pass