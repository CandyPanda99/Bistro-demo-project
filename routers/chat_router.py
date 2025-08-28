from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from schemas.chat_request import ChatRequest
from schemas.chat_response import ChatResponse
from services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post(
    "/generate/chat/customer_support_agent",
    tags=["Bistro support agent"],
    description="Bistro agent that can answer questions about menus, orders, and reservations.",
)
def generate(request: ChatRequest) -> ChatResponse:
    response_content = chat_service.generate_response(request)
    return ChatResponse(response=response_content)

@router.post(
    "/generate/chat/customer_support_agent/stream",
    tags=["Bistro support agent"],
    description="Bistro agent that can answer questions about menus, orders, and reservations with streaming.",
)
async def generate_stream(request: ChatRequest):
    return StreamingResponse(chat_service.generate_streaming_response(request), media_type="text/event-stream")
