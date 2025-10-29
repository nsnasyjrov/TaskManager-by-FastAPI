import uuid
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.functions import func
from sqlalchemy.testing.schema import mapped_column
from app.models.base_model import BaseModel

class UserModel(BaseModel):
    """
    SQLAlchemy ORM model representing an application user.

    Attributes:
        id (int): Primary key. Unique identifier of the user.
        fullname (str): Full name of the user.
        username (str): Unique username used for authentication or display.
        password_hash (str): Hashed user password (never store plain text).
        email (str | None): User email address. Must be unique if provided.
        active (bool): Indicates whether the user account is active.
        role (str): User role (e.g., 'admin', 'user', 'moderator').
        created_at (datetime.date): Date when the record was created.
        updated_at (datetime.date | None): Date of the last update.

    Notes:
        - Passwords should always be stored as hashes using a secure algorithm.
        - Use `created_at` and `updated_at` for auditing and tracking changes.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    email:  Mapped[str] = mapped_column(String, unique=True)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(Date, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(Date)
    public_id: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid.uuid4()))

    def __repr__(self):
        return f"<User id={self.id} username={self.username!r} email={self.email!r}>"