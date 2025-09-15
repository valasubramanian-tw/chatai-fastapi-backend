import pytest
from src.services.chat_service import ChatService, SESSION_FILE, CHAT_FILE

@pytest.fixture(autouse=True)
def clean_stores(tmp_path, monkeypatch):
    # Use temp files for isolation
    session_file = tmp_path / "session_store.txt"
    chat_file = tmp_path / "chat_store.txt"
    monkeypatch.setattr("src.services.chat_service.SESSION_FILE", str(session_file))
    monkeypatch.setattr("src.services.chat_service.CHAT_FILE", str(chat_file))
    # Re-import to reload stores
    import importlib
    import src.services.chat_service as chat_service_module
    importlib.reload(chat_service_module)
    yield

def test_create_session():
    service = ChatService()
    session = service.create_session("UserTest")
    assert session["session_user"] == "usertest"
    assert "session_id" in session
    assert "created_at" in session

def test_add_and_get_message():
    service = ChatService()
    session = service.create_session("UserTest")
    session_id = session["session_id"]
    service.add_message(session_id, "user", "Hello!")
    messages = service.get_messages(session_id)
    assert len(messages) == 1
    assert messages[0]["role"] == "user"
    assert messages[0]["content"] == "Hello!"

def test_get_messages_with_role_filter():
    service = ChatService()
    session = service.create_session("UserTest")
    session_id = session["session_id"]
    service.add_message(session_id, "user", "Hi")
    service.add_message(session_id, "assistant", "Hello!")
    user_msgs = service.get_messages(session_id, role="user")
    assert len(user_msgs) == 1
    assert user_msgs[0]["role"] == "user"

def test_add_message_invalid_session():
    service = ChatService()
    with pytest.raises(ValueError):
        service.add_message(999, "user", "Hello")

def test_get_messages_invalid_session():
    service = ChatService()
    with pytest.raises(ValueError):
        service.get_messages(999)