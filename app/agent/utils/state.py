from typing import Annotated, TypedDict, List
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # add_messages ensures new chat turns are appended to history
    messages: Annotated[List[BaseMessage], add_messages]
    user_id: str
    current_action: str  # e.g., "searching", "booking", "answering"
    context: str
