from sqlalchemy import BigInteger, Column, Date, DateTime, MetaData, String, Table

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("document", String(14), nullable=False),
    Column("email", String(100), nullable=False),
    Column("email_verified_at", DateTime, nullable=False),
    Column("phone", String(15)),
    Column("phone_verified_at", DateTime),
    Column("hashed_password", String(60), nullable=False),
    Column("birth_date", Date, nullable=False),
    Column("picture_url", String(255)),
    Column("last_login_at", DateTime),
)
