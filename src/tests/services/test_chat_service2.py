# import pytest

# def test_create_session(chat_service):
#     session = chat_service.create_session("UserTest")
#     assert session["session_user"] == "usertest"
#     assert "session_id" in session
#     assert "created_at" in session

# def test_add_and_get_message(chat_service):
#     session = chat_service.create_session("UserTest")
#     session_id = session["session_id"]
#     chat_service.add_message(session_id, "user", "Hello!")
#     messages = chat_service.get_messages(session_id)
#     assert len(messages) == 1
#     assert messages[0]["role"] == "user"
#     assert messages[0]["content"] == "Hello!"

# def test_get_messages_with_role_filter(chat_service):
#     session = chat_service.create_session("UserTest")
#     session_id = session["session_id"]
#     chat_service.add_message(session_id, "user", "Hi")
#     chat_service.add_message(session_id, "assistant", "Hello!")
#     user_msgs = chat_service.get_messages(session_id, role="user")
#     assert len(user_msgs) == 1
#     assert user_msgs[0]["role"] == "user"

# def test_add_message_invalid_session(chat_service):
#     with pytest.raises(ValueError):
#         chat_service.add_message(999, "user", "Hello")

# def test_get_messages_invalid_session(chat_service):
#     with pytest.raises(ValueError):
#         chat_service.get_messages(999)