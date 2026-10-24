from google import genai
from google.genai import types

from app.core.config import settings


class EmbeddingProviderError(Exception):
    pass

def generate_embedding(
        text: str,
        task_type: str = "RETRIEVAL_DOCUMENT"
):
    if not settings.gemini_api_key:
        raise EmbeddingProviderError(
            "Gemini API key is not configured."
        )

    if not text.split():
        raise ValueError(
            "input to generate embedding is empty"
        )

    try:
        client = genai.Client(api_key=settings.gemini_api_key)

        response = client.models.embed_content(
            model = settings.gemini_embedding_model,
            contents= text,
            config = types.EmbedContentConfig(
                task_type= task_type,
                output_dimensionality= settings.embedding_dimensions
            )
        )

        if not response.embeddings:
            raise EmbeddingProviderError("embedding provider generated no embeddings")

        values = response.embeddings[0].values

        if values is None or len(values) != settings.embedding_dimensions:
            raise EmbeddingProviderError(
                "embedding has an unexpected dimensions"
            )

        return list(values)

    except EmbeddingProviderError:
        raise
    except Exception as exc:
        raise EmbeddingProviderError(
            "Failed to generate embedding"
        ) from exc