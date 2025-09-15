# src/models/session.py
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class SessionCreateRequest(BaseModel):
    session_user: str = Field(min_length=1, max_length=10, description="Username for the session")
    
    @field_validator("session_user")
    def validate_session_user(cls, v):
        stripped_value = v.strip()
        if not stripped_value:
            raise ValueError("Username cannot be empty")
        if not stripped_value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return stripped_value
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "session_user": "user123"
            }
        }
    }

class SessionResponse(BaseModel):
    session_id: int
    session_user: str
    created_at: datetime
