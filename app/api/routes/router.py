from fastapi import APIRouter
from app.controllers import tickets_controller as ticket

api_router = APIRouter()
api_router.include_router(ticket.router, tags=["ticket"], prefix="/tasks")
