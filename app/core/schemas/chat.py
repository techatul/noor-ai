from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    user_id: str
    thread_id: Optional[str] = "default_thread"

class ChatResponse(BaseModel):
    answer: str
    thread_id: str