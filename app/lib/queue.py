from typing import Any, Callable

from app.core.logging import get_logger

logger = get_logger(__name__)


class QueueService:
    def __init__(self) -> None:
        self._handlers: dict[str, Callable[..., Any]] = {}

    def register(self, task_name: str, handler: Callable[..., Any]) -> None:
        self._handlers[task_name] = handler

    def enqueue(self, task_name: str, *args: Any, **kwargs: Any) -> None:
        handler = self._handlers.get(task_name)
        if not handler:
            logger.error("No handler registered for task: %s", task_name)
            return
        logger.info("Enqueuing task: %s", task_name)
        # In production, delegate to Celery: celery_app.send_task(task_name, args=args, kwargs=kwargs)
