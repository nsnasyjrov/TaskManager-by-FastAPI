from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.dal.user_dal import UserDAL
from app.services.user_service import UserService

engine = create_async_engine(settings.database_url, echo=settings.debug)

AsyncSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncSession:
    async with AsyncSession() as session:
        yield session


class Container:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_dal = UserDAL(db)
        self.user_service = UserService(self.user_dal)