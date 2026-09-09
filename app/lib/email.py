from email.message import EmailMessage

import aiosmtplib

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class EmailService:
    async def send_email(self, to: str, subject: str, body: str) -> bool:
        if not settings.SMTP_HOST:
            logger.warning("SMTP not configured, skipping email to %s", to)
            return False

        message = EmailMessage()
        message["From"] = settings.EMAILS_FROM or settings.SMTP_USER
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)

        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASSWORD,
            start_tls=True,
        )
        return True
