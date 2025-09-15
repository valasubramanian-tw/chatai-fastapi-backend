
# GenAI Chat App Backend

Manage Chat Conversations for a GenAI Chat App using FastAPI

---

## ✅ Objective

This is a FastAPI service to:

- Create new chat sessions
- Add messages to a session
- Retrieve messages from a session

---

## ✅ API Endpoints

### 1. Create a New Chat Session

- **Endpoint:** `POST /sessions`
- **Request Body:**
  ```json
  {
    "session_user": "abc"
  }
  ```
- **Response:**
  ```json
  {
    "session_id": 2,
    "session_user": "abc",
    "created_at": "2025-06-30T16:05:00"
  }
  ```

---

### 2. Add a Message to a Session

- **Endpoint:** `POST /sessions/{session_id}/messages`
- **Request Body:**
  ```json
  {
    "role": "user",
    "content": "What is AI?"
  }
  ```

---

### 3. Get All Messages from a Session

- **Endpoint:** `GET /sessions/{session_id}/messages`
- **Response:**
  ```json
  [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
  ]
  ```

---

## ✅ Run app

```sh
uvicorn src.app:app --reload
```

---

## ✅ Run Unit Tests

```python
pytest
```
