from dataclasses import dataclass
from datetime import datetime

from identity.domain.utils import parse_iso_datetime


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

    def __post_init__(self) -> None:
        for field in self.__dataclass_fields__:
            if field.endswith("_at") or field.endswith("_date"):
                value = getattr(self, field)

                if value and not isinstance(value, datetime):
                    setattr(self, field, parse_iso_datetime(value))
