# src/routers/sessions.py
from fastapi import APIRouter, HTTPException, Path, Query
from typing import List, Optional
from starlette import status
from src.models.session import SessionCreateRequest, SessionResponse
from src.models.message import MessageCreateRequest, MessageResponse
from src.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/sessions", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(payload: SessionCreateRequest):
    try:
        session = chat_service.create_session(payload.session_user)
        return session
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/sessions/{session_id}/messages", status_code=status.HTTP_201_CREATED)
def add_message(
    payload: MessageCreateRequest,
    session_id: int = Path(gt=0, description="The ID of the session to add a message to"),
):
    try:
        chat_service.add_message(session_id, payload.role, payload.content)
        return {"message": "Message added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/sessions/{session_id}/messages", response_model=List[MessageResponse], status_code=status.HTTP_200_OK)
def get_messages(
    session_id: int = Path(gt=0, description="The ID of the session to retrieve messages from"),
    role: Optional[str] = Query(None, description="Filter by role (user or assistant)")
):
    try:
        messages = chat_service.get_messages(session_id, role)
        return messages
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
