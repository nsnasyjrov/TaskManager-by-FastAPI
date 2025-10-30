from fastapi import APIRouter

from app.api.user_routes.user_auth import user_auth_router

project_router = APIRouter(prefix="", tags=["projects"])

@project_router.get("/")
def index():
    """Main handler from project"""
    print("Тестовая запись")

# Added any routes from api
project_router.include_router(user_auth_router)