from app.core.response_classes import ResultFromBL
from app.dal.user_dal import UserDAL
from app.schemas.user.user_schema import UserCreateToDatabaseSchema
from app.core.logger import logger

class UserService:
    def __init__(self, user_dal: UserDAL):
        self.user_dal = user_dal

    async def create_user(self, user_data: UserCreateToDatabaseSchema):
        try:
            if await self.email_exist(user_data.email):
                return ResultFromBL(success=False, message="Email is already exists")

            await self.user_dal.create_user(user_data.model_dump())
            return ResultFromBL(success=True, message="User created")
        except Exception as e:
            logger.error(f"[UserService(create_user, 10)]: Exception when creating user method at business logic: {e}")
            return ResultFromBL(success=False, message="Exception in BL")

    async def email_exist(self, email_to_check):
        try:
            result = await self.user_dal.get_email(email_to_check)

            if result is not None:
                return True # email exist in db
            else:
                return False
        except Exception as e:
            logger.error(f"[UserService(email_exist, 14)]: Error when verifying email: {e}")
            raise