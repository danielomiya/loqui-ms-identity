from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    document: str
    birth_date: datetime
    email: str
    email_verified_at: datetime = None
    phone: str = None
    phone_verified_at: datetime = None
    hashed_password: bytes = None
    picture_url: str = None
    last_login_at: datetime = None
