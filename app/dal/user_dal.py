from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import logger
from app.models.user_model import UserModel

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
            logger.error(f"UserDAL(create_user, 13): Error when creating user: {e}")
            return None

    async def get_email(self, email_to_check: str):
        """This func return email from database if exists
        Args: verified_email(str)
        Returns: str/None"""
        try:
           stmt = select(UserModel.email).where(UserModel.email==email_to_check)
           result = await self.db_session.execute(stmt)
           email = result.scalar_one_or_none()

           return email
        except SQLAlchemyError as e:
            logger.error(f"[UserDAL(get_email, 27)]:Error when getting email: {e}")
            raise
        except Exception as e:
            logger.error(f"[UserDAL(get_email, 27)]:Database error: {e}")
