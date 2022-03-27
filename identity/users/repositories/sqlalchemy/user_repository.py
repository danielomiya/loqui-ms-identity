from dataclasses import asdict
from identity.domain.repositories.user_repository import (
    UserRepository as BaseUserRepository,
)
from identity.domain.models.user import User
from identity.users.repositories.sqlalchemy.base import SQLAlchemyMixin
from identity.users.repositories.sqlalchemy.tables import users


class UserRepository(BaseUserRepository, SQLAlchemyMixin):
    def store(self, entity: User) -> None:
        stmt = users.insert()
        print("stmt:", stmt)
        with self.get_conn() as conn:
            res = conn.execute(stmt, asdict(entity))
        entity.id = res.inserted_primary_key[0]

    def get_by_id(self, id: int) -> User:
        stmt = users.select().where(users.c.id == id)

        with self.get_conn() as conn:
            row = conn.execute(stmt).fetchone()

        if not row:
            return None

        return User(**row._asdict())
