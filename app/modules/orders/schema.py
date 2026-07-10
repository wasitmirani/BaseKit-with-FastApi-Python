from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.common.enums import OrderStatus


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: Decimal

    model_config = {"from_attributes": True}


class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total_amount: Decimal
    created_at: datetime
    items: list[OrderItemResponse] = []

    model_config = {"from_attributes": True}


class OrderStatusUpdate(BaseModel):
    status: OrderStatus
