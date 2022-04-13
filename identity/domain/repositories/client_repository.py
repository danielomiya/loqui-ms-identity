from identity.domain.models.client import Client
from identity.domain.repositories.base_repository import BaseRepository


class ClientRepository(BaseRepository[Client]):
    """
    Repository of application clients
    """
