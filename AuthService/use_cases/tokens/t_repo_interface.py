from abc import ABC, abstractmethod



class TokenRepoInterface(ABC):

    @abstractmethod
    async def save(self, refresh_token: str, user_id:int):
        pass

    @abstractmethod
    async def get(self, user_id:int):
        pass

    @abstractmethod
    async def delete(self, user_id:int):
        pass