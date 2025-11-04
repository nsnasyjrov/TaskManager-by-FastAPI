from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.core.logger import logger
from app.core.enums import UserRole
from app.utils.common_methods import bcrypt_hash_password


class UserCreateValidateSchema(BaseModel):
    """Validate json data in create method(handler)"""
    fullname: str
    username: str
    password: str
    email: Optional[str] = None

class UserCreateToDatabaseSchema(BaseModel):
    """If UserCreateValidateSchema true this schema create and send model_dump() to database"""
    fullname: str
    username: str
    password_hash: str
    email: Optional[str] = None
    active: bool = True
    role: UserRole = UserRole.USER.value
    created_at: datetime =  Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    @classmethod
    def create_schema(self, handler_schema:  UserCreateValidateSchema):
        try:
            dict_data = handler_schema.dict()
            hash_pass = bcrypt_hash_password(dict_data.pop("password"))

            dict_data["password_hash"] = hash_pass

            new_model = UserCreateToDatabaseSchema(**dict_data)
            return new_model
        except Exception as e:
            logger.error(f"[UserCreateToDatabaseSchema(create_schema)] Error when creating to db schema: {e}")
            raise