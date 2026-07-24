from domain.exceptions.account_exceptions import AccountNotExistsException, AccountAlreadyExistsException
from use_cases.accounts.a_dto_inp import AccountDTOInp
from use_cases.accounts.a_dto_out import AccountDTOOut


class AccountService:

    def __init__(self, account_repo):
        self.account_repo = account_repo

    async def get_account_by_wallet_id(self, wallet_id)->AccountDTOOut:
        a_out = await self.account_repo.get_account_by_wallet_id(wallet_id)
        if not a_out:
            raise AccountNotExistsException
        return AccountDTOOut(
            id=a_out.id,
            wallet_id=a_out.wallet_id,
            amount=a_out.amount
        )

    async def create(self, a_inp: AccountDTOInp) -> AccountDTOOut:
        a_out = await self.account_repo.create(a_inp)
        return AccountDTOOut(
            id=a_out.id,
            wallet_id=a_out.wallet_id,
            amount=a_out.amount
        )

