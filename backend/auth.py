from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET = "SECRET_KEY"
ALGO = "HS256"


pwd = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str):
    if password is None:
        password = ""
    if not isinstance(password, str):
        password = str(password)
    return pwd.hash(password)


def verify_password(password: str, hashed: str):
    if not isinstance(password, str):
        password = str(password)
    return pwd.verify(password, hashed)


def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(hours=3)})
    return jwt.encode(data, SECRET, ALGO)
