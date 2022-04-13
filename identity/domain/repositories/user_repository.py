from abc import ABCMeta, abstractmethod

from identity.domain.models.user import User
from identity.domain.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User], metaclass=ABCMeta):
    """
    Repository of users
    """

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        raise NotImplementedError("override me")
