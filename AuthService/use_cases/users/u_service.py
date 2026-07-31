from domain.exceptions.base_exceptions import ModelNotExistException, ModelAlreadyExistException
from use_cases.tokens.t_service_interface import TokenServiceInterface
from use_cases.uow.uow_interface import UnitOfWorkInterface
from use_cases.users.c_u_dto_inp import CreateUserDTOInp
from use_cases.users.g_u_dto_out import GetUserDTOOut
from use_cases.users.l_u_dto_inp import LoginUserDTOInp
from use_cases.users.u_dto_out import UserDTOOut
from use_cases.users.u_repo_interface import UserRepoInterface


class UserService:

    def __init__(self, user_repo: UserRepoInterface,
                 token_service: TokenServiceInterface,
                 uow: UnitOfWorkInterface
                 ):
        self.user_repo = user_repo
        self.token_service = token_service
        self.uow = uow

    async def get_by_email(self, email: str) -> GetUserDTOOut:
        async with self.uow:
            u_out = await self.user_repo.get_by_email(email)
            if not u_out:
                raise ModelNotExistException
            return GetUserDTOOut(**u_out.model_dump())

    async def create(self, u_inp: CreateUserDTOInp)->UserDTOOut:
        async with self.uow:

            u_out = await self.user_repo.get_by_email(u_inp.email)
            if u_out:
                raise ModelAlreadyExistException
            u_out = await self.user_repo.create(u_inp)
            tokens = await self.token_service.create(u_out.id)
            return UserDTOOut(
                id=u_out.id,
                email=u_out.email,
                name=u_out.name,
                access_token=tokens["access_token"],
                refresh_token=tokens["refresh_token"],
                token_type=tokens["token_type"]
            )

    async def login(self, u_inp: LoginUserDTOInp)->UserDTOOut | None:
        async with self.uow:
            u_out = await self.user_repo.get_by_email(u_inp.email)
            if not u_out:
                return None
            tokens = await self.token_service.create(u_out.id)
            return UserDTOOut(
                id=u_out.id,
                email=u_out.email,
                name=u_out.name,
                access_token=tokens["access_token"],
                refresh_token=tokens["refresh_token"],
                token_type=tokens["token_type"]
            )

    async def logout(self, user_id: int)->None:
        await self.token_service.delete(user_id)