from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import logger
from app.models.user_model import UserModel
from app.schemas.user.user_schema import UserCreateSchema

class UserDAL:
    """Data Access Layer for operations with UserModel"""
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, user_data: dict):
        """Create user in table user transaction"""
        user = UserModel(**user_data)
        try:
            self.db_session.add(user)
            await self.db_session.commit()
            await self.db_session.refresh(user)
            return user
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            logger.error(f"Error when creating user: {user.public_id}")
            return None
