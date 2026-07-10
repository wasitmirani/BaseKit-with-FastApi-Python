from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.modules.products.model import Product


class ProductRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, product_id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def list_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
        return self.db.query(Product).offset(skip).limit(limit).all()

    def create(self, product: Product) -> Product:
        now = datetime.now(timezone.utc)
        product.created_at = now
        product.updated_at = now
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, product: Product) -> Product:
        product.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product: Product) -> None:
        self.db.delete(product)
        self.db.commit()
