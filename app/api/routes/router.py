from fastapi import APIRouter

from app.controllers import tickets_controller as ticket
from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(ticket.router, tags=["ticket"], prefix="/ticket")
