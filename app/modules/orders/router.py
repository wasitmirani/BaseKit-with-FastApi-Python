from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_current_active_superuser, get_current_user, get_db
from app.modules.orders.schema import OrderCreate, OrderResponse, OrderStatusUpdate
from app.modules.orders.service import OrderService
from app.modules.users.model import User

router = APIRouter()


def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)


@router.post("/")
def create_order(
    payload: OrderCreate,
    current_user: User = Depends(get_current_user),
    service: OrderService = Depends(get_order_service),
):
    order = service.create_order(current_user.id, payload)
    return success_response(data=OrderResponse.model_validate(order).model_dump())


@router.get("/")
def list_orders(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    service: OrderService = Depends(get_order_service),
):
    orders = service.list_orders(current_user.id, skip=skip, limit=limit)
    data = [OrderResponse.model_validate(order).model_dump() for order in orders]
    return success_response(data=data)


@router.get("/{order_id}")
def get_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    service: OrderService = Depends(get_order_service),
):
    order = service.get_order(order_id, user_id=current_user.id)
    return success_response(data=OrderResponse.model_validate(order).model_dump())


@router.patch("/{order_id}/status")
def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    _: User = Depends(get_current_active_superuser),
    service: OrderService = Depends(get_order_service),
):
    order = service.update_status(order_id, payload)
    return success_response(data=OrderResponse.model_validate(order).model_dump())
