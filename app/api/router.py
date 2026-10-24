


from fastapi import APIRouter
from app.api.routes.inquiries import router as inquiries_router
from app.api.routes.chat import router as chat_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(inquiries_router)
api_router.include_router(chat_router)