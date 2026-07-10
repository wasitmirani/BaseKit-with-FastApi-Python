from decimal import Decimal

from sqlalchemy.orm import Session

from app.common.enums import OrderStatus
from app.common.exceptions import NotFoundException
from app.modules.orders.model import Order, OrderItem
from app.modules.orders.repository import OrderRepository
from app.modules.orders.schema import OrderCreate, OrderStatusUpdate
from app.modules.products.repository import ProductRepository


class OrderService:
    def __init__(self, db: Session) -> None:
        self.repo = OrderRepository(db)
        self.product_repo = ProductRepository(db)

    def create_order(self, user_id: int, payload: OrderCreate) -> Order:
        total = Decimal("0.00")
        order_items: list[OrderItem] = []

        for item in payload.items:
            product = self.product_repo.get_by_id(item.product_id)
            if not product:
                raise NotFoundException(f"Product {item.product_id} not found")

            line_total = product.price * item.quantity
            total += line_total
            order_items.append(
                OrderItem(
                    product_id=product.id,
                    quantity=item.quantity,
                    unit_price=product.price,
                )
            )

        order = Order(user_id=user_id, status=OrderStatus.PENDING, total_amount=total)
        return self.repo.create(order, order_items)

    def get_order(self, order_id: int, user_id: int | None = None) -> Order:
        order = self.repo.get_by_id(order_id)
        if not order or (user_id is not None and order.user_id != user_id):
            raise NotFoundException("Order not found")
        return order

    def list_orders(self, user_id: int, skip: int = 0, limit: int = 100) -> list[Order]:
        return self.repo.list_by_user(user_id, skip=skip, limit=limit)

    def update_status(self, order_id: int, payload: OrderStatusUpdate) -> Order:
        order = self.get_order(order_id)
        order.status = payload.status
        return self.repo.update(order)
