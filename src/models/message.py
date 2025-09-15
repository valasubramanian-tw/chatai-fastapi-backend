# src/models/message.py
from pydantic import BaseModel, Field
from typing import Literal

class MessageCreateRequest(BaseModel):
    role: Literal["user", "assistant"] = Field(description="Role of the message sender, either 'user' or 'assistant'")
    content: str = Field(min_length=1, description="Content of the message")

class MessageResponse(BaseModel):
    role: Literal["user", "assistant"]
    content: str
