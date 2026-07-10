from app.core.logging import get_logger

logger = get_logger(__name__)


class SMSService:
    async def send_sms(self, phone: str, message: str) -> bool:
        logger.info("Sending SMS to %s: %s", phone, message)
        # Integrate with Twilio, AWS SNS, etc.
        return True
