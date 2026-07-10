from app.workers.celery_app import celery_app


@celery_app.task(name="send_email")
def send_email_task(to: str, subject: str, body: str) -> bool:
    import asyncio

    from app.services.email import EmailService

    return asyncio.run(EmailService().send_email(to, subject, body))
