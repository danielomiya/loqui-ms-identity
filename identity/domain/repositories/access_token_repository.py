from abc import ABCMeta

from identity.domain.models.access_token import AccessToken
from identity.domain.repositories.base_repository import BaseRepository


class AccessTokenRepository(BaseRepository[AccessToken], metaclass=ABCMeta):
    """
    Repository of access tokens
    """
