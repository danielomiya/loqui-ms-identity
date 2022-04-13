from abc import ABCMeta

from identity.domain.models.token import Token
from identity.domain.repositories.base_repository import BaseRepository


class TokenRepository(BaseRepository[Token], metaclass=ABCMeta):
    """
    Repository of tokens
    """
