import json
from typing import Any

import redis

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class RedisService:
    def __init__(self) -> None:
        self._client: redis.Redis | None = None

    @property
    def client(self) -> redis.Redis | None:
        if not settings.REDIS_URL:
            return None
        if self._client is None:
            self._client = redis.from_url(str(settings.REDIS_URL), decode_responses=True)
        return self._client

    def set(self, key: str, value: Any, ttl: int | None = None) -> bool:
        if not self.client:
            logger.warning("Redis not configured")
            return False
        payload = json.dumps(value)
        if ttl:
            return bool(self.client.setex(key, ttl, payload))
        return bool(self.client.set(key, payload))

    def get(self, key: str) -> Any | None:
        if not self.client:
            return None
        value = self.client.get(key)
        return json.loads(value) if value else None

    def delete(self, key: str) -> bool:
        if not self.client:
            return False
        return bool(self.client.delete(key))
