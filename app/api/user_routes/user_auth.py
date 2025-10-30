from fastapi import APIRouter, Request

from app.schemas.user.user_schema import UserCreateValidateSchema

user_auth_router = APIRouter(prefix="/auth", tags=["users"])

@user_auth_router.post("/login")
async def authorization():
    """Доделать метод авторизации через JWT-токен, перенаправляя
        на метод создания пользователя

        предусмотреть разные способы авторизации:
        - по почте
        - по номеру телефона
        - по юзернейму
        - по приглашению

        то же самое впоследствии распространяется на регистрацию"""
@user_auth_router.post(("/register"))
async def register(user_schema: UserCreateValidateSchema, request: Request):
    user_service = request.state.container.user_service
    user = await user_service.create_user(user_schema)

    return {"message": "User created", "user_id": user.id}