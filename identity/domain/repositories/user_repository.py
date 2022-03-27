from abc import ABCMeta

from identity.domain.models.user import User
from identity.domain.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User], metaclass=ABCMeta):
    pass
