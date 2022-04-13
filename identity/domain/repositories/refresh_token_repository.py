from abc import ABCMeta

from identity.domain.models.refresh_token import RefreshToken
from identity.domain.repositories.base_repository import BaseRepository


class RefreshTokenRepository(BaseRepository[RefreshToken], metaclass=ABCMeta):
    """
    Repository of refresh tokens
    """
