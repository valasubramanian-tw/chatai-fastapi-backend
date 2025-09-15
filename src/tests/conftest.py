import os
import sys

# # Add the project root (one level above 'src') to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from src.app import app
from fastapi.testclient import TestClient
from src.services.chat_service import ChatService, SESSION_FILE, CHAT_FILE

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client
        
@pytest.fixture(scope="module")
def chat_service():
    # Ensure the session and chat files are clean before each test
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)
    
    service = ChatService()
    yield service
    
    # Clean up after tests
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)
        
@pytest.fixture(scope="module")
def chat_service_with_session():
    # Create a ChatService instance with an existing session
    service = ChatService()
    service.session = {"messages": []}
    yield service
    
    # Clean up after tests
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)