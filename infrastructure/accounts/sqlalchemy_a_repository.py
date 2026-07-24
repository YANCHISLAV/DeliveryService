from sqlalchemy import select

from domain.entities.account import Account
from infrastructure.accounts.a_model import AccountModel
from use_cases.accounts.a_repo_interface import AccountRepoInterface


class SQLAlchemyAccountRepository(AccountRepoInterface):

    def __init__(self, session):
        self.session = session

    async def get_by_wallet_id(self, wallet_id):
        query = select(AccountModel).where(AccountModel.wallet_id == wallet_id)
        query_res = await self.session.execute(query)
        model = query_res.scalar()
        return Account.model_validate(model)

    async def create(self, account: Account):
        account = AccountModel(**account.model_dump())
        self.session.add(account)
        await self.session.flush()
        await self.session.refresh(account)
        return Account.model_validate(account)

