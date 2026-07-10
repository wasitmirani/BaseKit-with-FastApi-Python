from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_current_active_superuser, get_db
from app.modules.products.schema import ProductCreate, ProductResponse, ProductUpdate
from app.modules.products.service import ProductService
from app.modules.users.model import User

router = APIRouter()


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


@router.get("/")
def list_products(
    skip: int = 0,
    limit: int = 100,
    service: ProductService = Depends(get_product_service),
):
    products = service.list_products(skip=skip, limit=limit)
    data = [ProductResponse.model_validate(product).model_dump() for product in products]
    return success_response(data=data)


@router.get("/{product_id}")
def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    product = service.get_product(product_id)
    return success_response(data=ProductResponse.model_validate(product).model_dump())


@router.post("/")
def create_product(
    payload: ProductCreate,
    _: User = Depends(get_current_active_superuser),
    service: ProductService = Depends(get_product_service),
):
    product = service.create_product(payload)
    return success_response(data=ProductResponse.model_validate(product).model_dump())


@router.patch("/{product_id}")
def update_product(
    product_id: int,
    payload: ProductUpdate,
    _: User = Depends(get_current_active_superuser),
    service: ProductService = Depends(get_product_service),
):
    product = service.update_product(product_id, payload)
    return success_response(data=ProductResponse.model_validate(product).model_dump())


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    _: User = Depends(get_current_active_superuser),
    service: ProductService = Depends(get_product_service),
):
    service.delete_product(product_id)
    return success_response(message="Product deleted successfully")
