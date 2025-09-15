# src/app.py

from fastapi import FastAPI
from src.routers.sessions import router as sessions_router

app = FastAPI()

app.include_router(sessions_router)
