from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .nodes import retrieve, generate
# from IPython.display import Image, display


# Build workflow
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

# Add edges to connect nodes
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile
chain = workflow.compile()