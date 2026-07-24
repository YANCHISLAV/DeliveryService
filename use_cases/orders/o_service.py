from domain.exceptions.base_exceptions import ModelNotExistException, ModelAlreadyExistException
from use_cases.orders.o_dto_inp import OrderDTOInp
from use_cases.orders.o_dto_out import OrderDTOOut


class OrderService:
    def __init__(self, order_repo):
        self.order_repo = order_repo

    async def get_by_user_id(self, order: OrderDTOInp)->OrderDTOOut:
        o_out = await self.order_repo.get_by_user_id(order.user_id)
        if not o_out:
            raise ModelNotExistException("order")
        return OrderDTOOut(
            **o_out.model_dump()
        )

    async def create(self, order: OrderDTOInp)->OrderDTOOut:
        try:
            await self.order_repo.get_by_user_id(order.user_id)
        except ModelNotExistException("order"):
            o_out = self.order_repo.create(order)
            return OrderDTOOut(
                **o_out.model_dump()
            )
        raise ModelAlreadyExistException("order")



