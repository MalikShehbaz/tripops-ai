

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService, AIProviderError, AIConfigurationError


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    service = ChatService()

    try:
        answer = service.get_response(request.message)
        return ChatResponse(message = answer)
    except AIConfigurationError:
        raise HTTPException(
            status_code = 503,
            detail= "AI assistant is not configured"      
        )
    except AIProviderError:
        raise HTTPException(
            status_code= 502,
            detail= "AI Assistant could not generate response"
        )