from app.workers.celery_app import celery_app


@celery_app.task(name="send_notification")
def send_notification_task(user_id: int, message: str) -> dict:
    return {"user_id": user_id, "message": message, "status": "sent"}
