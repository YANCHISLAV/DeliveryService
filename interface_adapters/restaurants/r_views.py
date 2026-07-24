
from fastapi import APIRouter, Depends

from interface_adapters.restaurants.r_dpns import i_restaurant_service
from interface_adapters.restaurants.r_dto_req import RestaurantDTOReq
from interface_adapters.restaurants.r_dto_res import RestaurantDTORes
from use_cases.restaurant.r_dto_inp import RestaurantDTOInp
from use_cases.restaurant.r_service import RestaurantService

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.get("/address")
async def get_by_address(restaurant: RestaurantDTOReq, restaurant_service: RestaurantService = Depends(i_restaurant_service))->RestaurantDTORes:
    restaurant = await restaurant_service.get_by_address(RestaurantDTOInp(**restaurant.model_dump()))
    return RestaurantDTORes(**restaurant.model_dump())

@router.post("/")
async def create(restaurant: RestaurantDTOReq, restaurant_service: RestaurantService = Depends(i_restaurant_service))->RestaurantDTORes:
    restaurant = await restaurant_service.create(RestaurantDTOInp(**restaurant.model_dump()))
    return RestaurantDTORes(**restaurant.model_dump())