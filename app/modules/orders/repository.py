from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.modules.orders.model import Order, OrderItem


class OrderRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, order_id: int) -> Order | None:
        return self.db.query(Order).filter(Order.id == order_id).first()

    def list_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> list[Order]:
        return (
            self.db.query(Order)
            .filter(Order.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, order: Order, items: list[OrderItem]) -> Order:
        now = datetime.now(timezone.utc)
        order.created_at = now
        order.updated_at = now
        self.db.add(order)
        self.db.flush()

        for item in items:
            item.order_id = order.id
            self.db.add(item)

        self.db.commit()
        self.db.refresh(order)
        return order

    def update(self, order: Order) -> Order:
        order.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(order)
        return order
