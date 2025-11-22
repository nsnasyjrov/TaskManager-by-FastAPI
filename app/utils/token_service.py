import os
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv

load_dotenv()

DEFAULT_SECRET_KEY = os.getenv("DEFAULT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
DEFAULT_EXP_MINUTES = 30

class TokenService:
    def __init__(self, secret_key: str = DEFAULT_SECRET_KEY, algorithm: str = JWT_ALGORITHM):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_access_token(self, user_id: int):
        payload = {
            "sub": str(user_id),
            "exp": datetime.now() + timedelta(minutes=DEFAULT_EXP_MINUTES)
        }
        return jwt.encode(payload, user_id, JWT_ALGORITHM)