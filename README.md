
# GenAI Chat App Backend

Manage Chat Conversations for a GenAI Chat App using FastAPI

---

## ✅ Objective

Implement a FastAPI service to:

- Create new chat sessions
- Add messages to a session
- Retrieve messages from a session

> **Note:** No database required — use in-memory Python data structures.

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
- **Behavior:**
  - Add validation: Reject empty usernames.
  - Normalize username input (remove trailing spaces and convert to lowercase)
  - Assign `session_id = len(session_store) + 1`
  - Set `created_at` to current UTC timestamp
  - Add new entry to `session_store`
  - Initialize empty list in `chat_store[session_id]`

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
- **Behavior:**
  - Validates if session exists
  - Validates if role is `user` or `assistant`
  - Appends message to `chat_store[session_id]`
  - Raise Exception if session ID doesn’t exist or role is not valid

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
- **Behavior:**
  - Returns full chat history for the session
  - Add filtering by role using query param (use list comprehension)
  - Raises Exception if session not found

---

## ✅ Run app

```sh
uvicorn src.app:app --reload
```

---

## ✅ Add Unit Tests

Consider adding tests for the above endpoints using pytest.
