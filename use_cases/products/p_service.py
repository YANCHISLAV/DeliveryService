from domain.exceptions.base_exceptions import ModelNotExistException
from domain.exceptions.product_exceptions import ProductNotExistsException, ProductAlreadyExistsException
from use_cases.products.p_dto_inp import ProductDTOInp
from use_cases.products.p_dto_out import ProductDTOOut
from use_cases.products.p_exists_dto_inp import ProductExistsDTOInp
from use_cases.products.p_filters_dto_inp import ProductFiltersDTOInp


class ProductService:

    def __init__(self, product_repo):
        self.product_repo = product_repo

    async def get_by_id(self, p_id: int)->ProductDTOOut:

        p_out = await self.product_repo.get_by_id(p_id)
        if not p_out:
            raise ProductNotExistsException
        return ProductDTOOut(
            **p_out.model_dump()
        )

    async def get_by_filters(self, p_inp)->ProductDTOOut:
        p_out = await self.product_repo.get_by_filters(p_inp)
        if not p_out:
            raise ProductNotExistsException
        return ProductDTOOut(
            **p_out.model_dump()
        )

    async def get_by_restaurant_id_and_name(self, p_inp)->ProductDTOOut:
        p_out = await self.product_repo.get_by_restaurant_id_and_name(p_inp)
        if not p_out:
            raise ModelNotExistException
        return ProductDTOOut(
            **p_out.model_dump()
        )

    async def create(self, p_inp: ProductExistsDTOInp)->ProductDTOOut:
        try:
            await self.product_repo.get_by_restaurant_id_and_name(p_inp)
        except ProductNotExistsException:
            p_out = self.product_repo.create(p_inp)
            return ProductDTOOut(
                **p_out.model_dump()
            )
        raise ProductAlreadyExistsException