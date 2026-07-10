from sqlalchemy.orm import Session

from app.common.exceptions import NotFoundException
from app.modules.products.model import Product
from app.modules.products.repository import ProductRepository
from app.modules.products.schema import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session) -> None:
        self.repo = ProductRepository(db)

    def get_product(self, product_id: int) -> Product:
        product = self.repo.get_by_id(product_id)
        if not product:
            raise NotFoundException("Product not found")
        return product

    def list_products(self, skip: int = 0, limit: int = 100) -> list[Product]:
        return self.repo.list_all(skip=skip, limit=limit)

    def create_product(self, payload: ProductCreate) -> Product:
        product = Product(**payload.model_dump())
        return self.repo.create(product)

    def update_product(self, product_id: int, payload: ProductUpdate) -> Product:
        product = self.get_product(product_id)
        update_data = payload.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(product, field, value)
        return self.repo.update(product)

    def delete_product(self, product_id: int) -> None:
        product = self.get_product(product_id)
        self.repo.delete(product)
