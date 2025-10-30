from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dal.user_dal import UserDAL
from app.services.user_service import UserService


class DependenciesInProject:
    def get_user_service(db: AsyncSession = Depends(get_db)):
        user_dal = UserDAL(db)
        service = UserService(user_dal)
        return service
