from abc import ABC, abstractmethod

from domain.entities.account import Account


class AccountRepoInterface(ABC):

    @abstractmethod
    async def get_by_wallet_id(self, wallet_id: int) -> Account:
        pass

    @abstractmethod
    async def create(self, account) -> Account:
        pass