from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from app.core.enums import UserRole

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
    password: str
    email: Optional[str] = None
    active: bool
    role: UserRole
    created_at: datetime
    updated_at: Optional[datetime] = None
