from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)


class AIService:
    async def generate_text(self, prompt: str, **kwargs: Any) -> str:
        logger.info("AI generate_text called")
        # Integrate with OpenAI, Anthropic, etc.
        return f"Generated response for: {prompt[:50]}..."

    async def embed(self, text: str) -> list[float]:
        logger.info("AI embed called")
        return [0.0] * 1536
