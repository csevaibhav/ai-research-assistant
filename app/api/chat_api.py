from fastapi import APIRouter, Depends

from app.dependencies.llm import get_chat_service
from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    answer = chat_service.ask(request.question)

    return ChatResponse(answer=answer)