from .state import AgentState
from app.core.config import getAppConfig
from langchain.chat_models import init_chat_model
from app.core.schemas.agent import AssistantResponse
from langchain_core.messages import SystemMessage, HumanMessage
from app.db.vectordb import load_vectorstore


# Initializing once at the module level
config = getAppConfig()
shared_model = init_chat_model(
    config.GROQ_MODEL,
    model_provider="groq",
    api_key=config.GROQ_API_KEY
)

# retrive data from vectordb
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Bind the structure to the model once
structured_llm = shared_model.with_structured_output(AssistantResponse)

async def retrieve(state: AgentState):
    """Fetch relevant docs from the vector store."""
    last_message = state["messages"][-1].content
    docs = await retriever.ainvoke(last_message)
    context = "\n\n".join([d.page_content for d in docs])
    return {"context": context}

async def generate(state: AgentState):
    """Generate an answer based on context."""
    system_prompt = f"""
    You are Noor-AI, the official virtual assistant for Kisha Haldia's makeup business.
    Answer the user's questions strictly using the provided context.
    
    Context:
    {state['context']}
    
    If the answer isn't in the context, politely say you don't know and offer to connect them with a human.
    """
    
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    response = await structured_llm.ainvoke(messages)
    return {
        "messages": [HumanMessage(content=response.answer)],
        "current_action": response.action,
        "confidence": response.confidence
    }

# async def call_model(state: AgentState):
#     """Decides what to do based on user input."""
#     messages = state["messages"]

#     # Optional: Add a system message to keep the bot in character
#     if not any(isinstance(m, SystemMessage) for m in messages):
#         messages = [SystemMessage(content="You are a helpful assistant for Kisha Haldia.")] + messages

#     response = await structured_llm.ainvoke(messages)
#     return {"messages": [response]}