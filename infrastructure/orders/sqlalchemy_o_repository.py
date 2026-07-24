from sqlalchemy import select

from domain.entities.order import Order
from infrastructure.orders.o_model import OrderModel
from use_cases.orders.o_repo_interface import OrderRepoInterface


class SQLAlchemyOrderRepository(OrderRepoInterface):
    def __init__(self, session):
        self.session = session

    async def get_by_user_id(self, user_id):
        query = select(OrderModel).where(OrderModel.user_id == user_id)
        query_res = await self.session.execute(query)
        model = query_res.scalar()
        return Order.model_validate(model)

    async def create(self, order: Order):
        model = OrderModel(**order.model_dump())
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return Order.model_validate(model)
