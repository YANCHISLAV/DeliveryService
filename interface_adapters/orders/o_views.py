
from fastapi import APIRouter

from domain.exceptions.base_exceptions import ModelAlreadyExistException
from interface_adapters.orders.o_dto_req import OrderDTOReq
from use_cases.orders.o_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/{user_id}")
async def get_by_user_id(user_id: int):
    pass

@router.post("/")
async def create(order: OrderDTOReq, order_service: OrderService):
    pass