from dataclasses import asdict
from typing import Any, Dict

from identity.domain.models.user import User
from identity.domain.repositories.user_repository import (
    UserRepository as BaseUserRepository,
)
from identity.users.repositories.sqlalchemy.base import SQLAlchemyMixin
from identity.users.repositories.sqlalchemy.tables import User as UserTable


class UserRepository(BaseUserRepository, SQLAlchemyMixin):
    def store(self, entity: User) -> None:
        user = UserTable(**asdict(entity))
        with self.get_session() as session:
            session.add(user)
            session.commit()

            # query newly inserted to get its id
            new_user = session.query(UserTable).filter_by(document=entity.document).first()
            entity.id = new_user.id

    def _get_first(self, **criterion: Dict[str, Any]) -> User:
        with self.get_session() as session:
            user = session.query(UserTable).filter_by(**criterion).first()

            if not user:
                return None

            return User(**dict(user))

    def get_by_id(self, id: int) -> User:
        return self._get_first(id=id)

    def get_by_email(self, email: str) -> User:
        return self._get_first(email=email)
