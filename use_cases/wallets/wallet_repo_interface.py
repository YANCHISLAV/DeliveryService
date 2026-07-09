from domain.wallet import Wallet
from abc import ABC, abstractmethod

class WalletRepoInterface(ABC):
    @abstractmethod
    def get_wallet_by_id(self, id: int)->Wallet:
        pass

    @abstractmethod
    def create_wallet_by_id(self, user_id)->Wallet:
        pass

    @abstractmethod
    def update_wallet_by_id(self)->Wallet:
        pass

    @abstractmethod
    def delete_wallet_by_id(self)->None:
        pass