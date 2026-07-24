from abc import ABC, abstractmethod

from domain.entities.transaction import Transaction


class TransactionRepoInterface(ABC):

    @abstractmethod
    async def create(self, transaction)->Transaction:
        pass

    @abstractmethod
    async def get_by_id(self, transaction_id) -> Transaction:
        pass