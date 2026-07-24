from domain.exceptions.base_exceptions import ModelNotExistException, ModelAlreadyExistException
from use_cases.restaurant.r_dto_inp import RestaurantDTOInp
from use_cases.restaurant.r_dto_out import RestaurantDTOOut


class RestaurantService:

    def __init__(self, restaurant_repo):
        self.restaurant_repo = restaurant_repo

    async def get_by_address(self, r_inp: RestaurantDTOInp)->RestaurantDTOOut:
        r_out = await self.restaurant_repo.get_by_address(r_inp)
        if not r_out:
            raise ModelNotExistException("restaurant")
        return RestaurantDTOOut(**r_out.model_dump())

    async def create(self, r_inp: RestaurantDTOInp)->RestaurantDTOOut:
        try:
            await self.restaurant_repo.get_by_address(r_inp)
        except ModelNotExistException("restaurant"):
            r_out = await self.restaurant_repo.create(r_inp)
            return RestaurantDTOOut(**r_out.model_dump())
        raise ModelAlreadyExistException("restaurant")