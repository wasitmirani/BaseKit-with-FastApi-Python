from enum import StrEnum


class UserRole(StrEnum):
    USER = "user"
    ADMIN = "admin"


class OrderStatus(StrEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class ProductStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    OUT_OF_STOCK = "out_of_stock"
