from fastapi import APIRouter, Request
from pydantic_core import ValidationError

from app.schemas.user.user_schema import UserCreateValidateSchema
from app.utils.common_methods import pydantic_errors
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
        json_data = await request.json()
        validate_schema = UserCreateValidateSchema(**json_data)
    except ValidationError as e:
        print("Пайдентик нашел ошибку")
        return ResultFromHandler.error(pydantic_errors(e), "Error when validate from client", 400)
    except Exception as e:
        return ResultFromHandler.error(e.__dict__, "Error when validate from client", 400)


    user_service = request.state.container.get_layer(exp_entity)
    #user = await user_service.create_user(user_schema)

    #return {"message": "User created", "user_id": user.id}