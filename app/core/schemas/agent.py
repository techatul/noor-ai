from pydantic import BaseModel, Field

# class AssistantResponse(BaseModel):
#     """Structured response from the AI assistant."""
#     answer: str = Field(description="The reply to the user")
#     is_booking_request: bool = Field(description="True if user wants to book")

# 1. Define the internal structure we want from the LLM
class AssistantResponse(BaseModel):
    answer: str = Field(description="The final answer to the user")
    action: str = Field(description="The action taken: 'searching', 'answering', or 'booking'")
    confidence: float = Field(description="Confidence score between 0 and 1")