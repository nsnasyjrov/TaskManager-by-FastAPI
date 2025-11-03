import json
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from app.utils.response_classes import ResultFromHandler

user_auth_router = APIRouter(prefix="/auth", tags=["users"])
exp_entity = "user"

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
async def register(request: Request):
    try:
        user_schema = await request.json()
    except json.JSONDecodeError as e:
        return ResultFromHandler.success(None, "Error validate data from client", 400)

    user_service = request.state.container.get_layer(exp_entity)
    user = await user_service.create_user(user_schema)

    return {"message": "User created", "user_id": user.id}