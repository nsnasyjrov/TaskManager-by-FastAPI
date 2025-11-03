from typing import Dict, Any, Type

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.logger import logger
from app.core.config import settings
from app.utils.common_methods import get_layers_from_utils

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
        self._cache = {}

    @property
    def get_layer(self, exp_entity: str):

        service_class, dal_class = get_layers_from_utils(exp_entity)

        if service_class == -1 or dal_class == -1:
            logger.error("[app/core/database.py] Container: error when getting layer")
            return -1

        dal_instance = dal_class(self.db)
        self._cache[exp_entity] = service_class(dal_instance)

        return self._cache[exp_entity]
