from sqlalchemy import BigInteger, Column, Date, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    document = Column(String(14), nullable=False)
    email = Column(String(100), nullable=False)
    email_verified_at = Column(DateTime)
    phone = Column(String(15))
    phone_verified_at = Column(DateTime)
    hashed_password = Column(String(60), nullable=False)
    birth_date = Column(Date, nullable=False)
    picture_url = Column(String(255))
    last_login_at = Column(DateTime)
