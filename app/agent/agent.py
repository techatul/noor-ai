from .utils.workflows import chain
# from IPython.display import Image, display

# Show workflow
# display(Image(chain.get_graph().draw_mermaid_png()))

async def initiate_chat(user_message: str, user_id: str):
    '''Initiate agent workflow'''
    inputs = {
        "messages": [("user", user_message)],
        "user_id": user_id
    }

    config = {"configurable": {"thread_id": user_id}}
    
    state = await chain.ainvoke(inputs, config=config)
    return state