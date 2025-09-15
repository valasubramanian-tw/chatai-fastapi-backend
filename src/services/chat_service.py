# src/services/chat_service.py
import os
import json
from datetime import datetime

SESSION_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../store/session_store.txt'))
CHAT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../store/chat_store.txt'))

def load_store(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default
    return default

def save_store(filename, store):
    with open(filename, 'w') as f:
        json.dump(store, f, default=str)

session_store = load_store(SESSION_FILE, {})
chat_store = load_store(CHAT_FILE, {})

class ChatService:
    def create_session(self, session_user: str) -> dict:
        normalized_user = session_user.lower()
        session_id = len(session_store) + 1
        created_at = datetime.now().isoformat()
        session = {
            "session_id": session_id,
            "session_user": normalized_user,
            "created_at": created_at,
        }
        session_store[str(session_id)] = session
        chat_store[str(session_id)] = []
        save_store(SESSION_FILE, session_store)
        save_store(CHAT_FILE, chat_store)
        return session

    def add_message(self, session_id: int, role: str, content: str):
        sid = str(session_id)
        if sid not in session_store:
            raise ValueError("Session not found.")
        chat_store[sid].append({"role": role, "content": content})
        save_store(CHAT_FILE, chat_store)

    def get_messages(self, session_id: int, role: str = None):
        sid = str(session_id)
        if sid not in session_store:
            raise ValueError("Session not found.")
        messages = chat_store[sid]
        if role:
            messages = [m for m in messages if m["role"] == role]
        return messages
