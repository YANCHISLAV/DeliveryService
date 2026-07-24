
from fastapi import APIRouter
from fastapi.params import Depends

from interface_adapters.products.p_dpns import i_product_service
from interface_adapters.products.p_dto_req import ProductDTOReq
from interface_adapters.products.p_dto_res import ProductDTORes
from interface_adapters.products.p_exists_dto_req import ProductExistsDTOReq
from interface_adapters.products.p_filters_dto_req import ProductFiltersDTOReq
from use_cases.products.p_dto_inp import ProductDTOInp
from use_cases.products.p_exists_dto_inp import ProductExistsDTOInp
from use_cases.products.p_filters_dto_inp import ProductFiltersDTOInp
from use_cases.products.p_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{p_id}")
async def get_by_id(product:ProductDTOReq, product_service: ProductService = Depends(i_product_service)):
     product = await product_service.get_by_id(product.id)
     return ProductDTORes(**product.model_dump())

@router.get("/filters")
async def get_by_filters(products: ProductFiltersDTOReq, product_service: ProductService = Depends(i_product_service)):
     products = await product_service.get_by_filters(products)
     return [ProductDTORes(**p.model_dump()) for p in products]


@router.post("/")
async def create(product: ProductExistsDTOReq,product_service: ProductService = Depends(i_product_service))->ProductDTORes:
     product = await product_service.create(
          ProductExistsDTOInp(
              **product.model_dump()
          )
     )
     return ProductDTORes(**product.model_dump())


