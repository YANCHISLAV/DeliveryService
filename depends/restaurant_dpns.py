from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.restaurants.sqlalchemy_r_repository import SQLAlchemyRestaurantRepository
from use_cases.restaurant.r_service import RestaurantService
from infrastructure.db.session import db

async def restaurant_service_provider(session: AsyncSession = Depends(db.get_session)) -> RestaurantService:
    restaurant_repo = SQLAlchemyRestaurantRepository(session)
    return RestaurantService(restaurant_repo=restaurant_repo)