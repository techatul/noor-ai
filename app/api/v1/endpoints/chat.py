from fastapi import APIRouter
from app.agent.agent import initiate_chat
from fastapi import APIRouter, HTTPException
from app.core.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/message", response_model=ChatResponse)
async def get_ai_response(request: ChatRequest):
    try:
        # call the agent service
        ai_response = await initiate_chat(request.message, request.user_id)

        # Return structured JSON
        return ChatResponse(
            answer=ai_response["messages"][-1].content,
            thread_id='123'
            # current_action=ai_response.get("current_action", "answering"),
            # confidence_score=ai_response.get("confidence", 1.0)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))