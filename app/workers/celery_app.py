from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "basekit",
    broker=settings.CELERY_BROKER_URL or "redis://localhost:6379/0",
    backend=settings.CELERY_RESULT_BACKEND or "redis://localhost:6379/0",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
)

celery_app.autodiscover_tasks(["app.workers"])
