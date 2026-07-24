from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.product import Product
from infrastructure.products.p_model import ProductModel
from interface_adapters.products.p_filters_dto_req import ProductFiltersDTOReq
from use_cases.products.p_repo_interface import ProductRepoInterface


class SQLAlchemyProductRepository(ProductRepoInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, p_id: int)->Product:
        query = select(ProductModel).where(ProductModel.id==p_id)
        query_res = await self.session.execute(query)
        model = query_res.scalar()
        return Product.model_validate(model)

    async def get_by_filters(self, products: ProductFiltersDTOReq)->list[Product]:
        query = select(ProductModel)
        if products.name:
            query = query.where(ProductModel.name == products.name)
        if products.min_price:
            query = query.where(ProductModel.price >= products.min_price)
        if products.max_price:
            query = query.where(ProductModel.price <= products.max_price)
        if products.category:
            query = query.where(ProductModel.category == products.category)
        if products.cuisine:
            query = query.where(ProductModel.cuisine == products.cuisine)
        query_res = await self.session.execute(query)
        model_list = query_res.scalars().all()
        return [Product.model_validate(model) for model in model_list]

    async def get_by_restaurant_id_and_name(self, product: Product)->Product:
        query = select(ProductModel).where(ProductModel.restaurant_id == product.restaurant_id)
        query_res = await self.session.execute(query)
        model = query_res.scalar()
        return Product.model_validate(model)

    async def create(self, product: Product) -> Product:
        model = ProductModel(**product.model_dump())
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return Product.model_validate(model)