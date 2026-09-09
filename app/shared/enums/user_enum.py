from enum import StrEnum


class UserRole(StrEnum):
    USER = "user"
    ADMIN = "admin"

class UserStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    BLOCKED = "blocked"
    DELETED = "deleted"
    VERIFIED = "verified"
    UNVERIFIED = "unverified"