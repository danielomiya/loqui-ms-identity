from dataclasses import asdict
from identity.domain.repositories.user_repository import (
    UserRepository as BaseUserRepository,
)
from identity.domain.models.user import User
from identity.users.repositories.sqlalchemy.base import SQLAlchemyMixin
from identity.users.repositories.sqlalchemy.tables import User as sqlUser


class UserRepository(BaseUserRepository, SQLAlchemyMixin):
    def store(self, entity: User) -> None:
        user = sqlUser(**asdict(entity))
        with self.get_session() as session:
            session.add(user)
            session.commit()

            # query newly inserted to get its id
            new_user = (
                session.query(sqlUser).filter_by(document=entity.document).first()
            )
            entity.id = new_user.id

    def get_by_id(self, id: int) -> User:
        session = self.get_session()
        user = session.query(sqlUser).filter_by(id=id).first()

        if not user:
            return None

        return User(**dict(user))
