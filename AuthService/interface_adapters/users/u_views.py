
from fastapi import APIRouter, Depends

from interface_adapters.users.c_u_dto_req import CreateUserDTOReq
from interface_adapters.users.u_dpns import i_user_service
from interface_adapters.users.u_dto_res import UserDTORes
from interface_adapters.users.l_user_dto_req import LoginUserDTOReq
from use_cases.users.c_u_dto_inp import CreateUserDTOInp
from use_cases.users.l_u_dto_inp import LoginUserDTOInp
from use_cases.users.u_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def get_by_id():
    pass

@router.post("/register")
async def create(user_req: CreateUserDTOReq, user_service: UserService = Depends(i_user_service))->UserDTORes:
    user_inp = CreateUserDTOInp(**user_req.model_dump())
    user_res = await user_service.create(user_inp)
    return UserDTORes(**user_res.model_dump())

@router.post("/login")
async def login(user_req: LoginUserDTOReq, user_service: UserService = Depends(i_user_service))->UserDTORes | str:
    user_inp = LoginUserDTOInp(**user_req.model_dump())
    user_res = await user_service.login(user_inp)
    if not user_res:
        return "Incorrect email or password"
    return UserDTORes(**user_res.model_dump())

@router.post("/logout")
async def logout(user_id: int, user_service: UserService = Depends(i_user_service))->None:
    await user_service.logout(user_id)