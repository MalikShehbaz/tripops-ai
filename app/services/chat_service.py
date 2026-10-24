
import logging
from google import genai

from app.ai.prompt import SYSTEM_PROMPT
from app.core.config import settings
from app.schemas.chat import ChatRequest


logger = logging.getLogger(__name__)

class AIConfigurationError(Exception):
    pass

class AIProviderError(Exception):
    pass


class ChatService:

    def get_response(self, message:str) -> str:

        if not settings.gemini_api_key:
            raise AIConfigurationError(
                "The AI provider is not configured."
            )

        try:
            client = genai.Client(api_key= settings.gemini_api_key)

            response = client.models.generate_content(
                 model = settings.gemini_model,
                 contents= (
                    f"{SYSTEM_PROMPT}\n\n",
                    f"traverler's message: {message}"
                  )
                )

            answer = response.text

            if not answer or not answer.strip():
                raise AIProviderError(
                    "AI provided response is empty"
                )

            return answer.strip()

        except AIProviderError:
            raise
        except Exception as exc:
            logger.exception("Gemini request failed")
            raise AIProviderError(
                "The AI provider request failed"
            ) from exc



