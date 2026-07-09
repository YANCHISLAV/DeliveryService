
from use_cases.wallets.wallet_dto_res import WalletDTORes
from use_cases.wallets.wallet_repo_interface import WalletRepoInterface

class WalletService:
    def __init__(self, wallet_repo: WalletRepoInterface):
        self.wallet_repo = wallet_repo
    def create(self, req) -> WalletDTORes:
        res = self.user_repo.create_wallet_by_id(id = req.id)
        return WalletDTORes(
            id = res.id,
            amount=res.amount
        )
    def get(self) -> WalletDTORes:
        pass
    def update(self) -> WalletDTORes:
        pass
    def delete(self) -> None:
        pass