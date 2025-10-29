from enum import Enum

class UserRole(Enum):
    """User role in application"""
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"