from datetime import datetime
from typing import Optional
from app.core.enums import UserRole
from app.models.base_model import BaseModel

class UserCreateSchema(BaseModel):
    """Create user schemavalidation"""
    fullname: str
    username: str
    password: str
    email: Optional[str] = None
    active: bool
    role: UserRole
    created_at: datetime
    updated_at: Optional[datetime] = None

