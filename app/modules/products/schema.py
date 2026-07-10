from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.common.enums import ProductStatus


class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = None
    price: Decimal = Field(gt=0)
    stock: int = Field(ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    status: ProductStatus | None = None


class ProductResponse(ProductBase):
    id: int
    status: ProductStatus
    created_at: datetime

    model_config = {"from_attributes": True}
