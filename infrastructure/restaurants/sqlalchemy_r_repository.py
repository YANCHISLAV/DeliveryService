from sqlalchemy import select

from domain.entities.restaurant import Restaurant
from infrastructure.restaurants.r_model import RestaurantModel
from use_cases.restaurant.r_repo_interface import RestaurantRepoInterface


class SQLAlchemyRestaurantRepository(RestaurantRepoInterface):
    def __init__(self, session):
        self.session = session

    async def get_by_address(self, restaurant) ->Restaurant:
        query = (select(RestaurantModel).where(RestaurantModel.name == restaurant.name ).
                      where(RestaurantModel.city == restaurant.city).
                      where(RestaurantModel.street == restaurant.street).
                      where(RestaurantModel.house_number == restaurant.house_number))
        query_res = await self.session.execute(query)
        restaurant = query_res.scalar()
        return Restaurant.model_validate(restaurant)


    async def create(self, restaurant) -> Restaurant:
        restaurant = RestaurantModel(**restaurant.model_dump())
        self.session.add(restaurant)
        await self.session.flush()
        await self.session.refresh(restaurant)
        return Restaurant.model_validate(restaurant)
