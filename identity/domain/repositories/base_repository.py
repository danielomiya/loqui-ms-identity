from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Union

T = TypeVar("T")
Id = Union[str, int]


class BaseReadRepository(Generic[T], metaclass=ABCMeta):
    """
    Read-only base repository
    """

    @abstractmethod
    def get_by_id(self, id: Id) -> T:
        """
        Gets an entity by id

        Args:
            id (Id): id of the entity

        Returns:
            T: entity itself
        """
        raise NotImplementedError("override me")


class BaseWriteRepository(Generic[T], metaclass=ABCMeta):
    """
    Write base repository
    """

    @abstractmethod
    def store(self, entity: T) -> None:
        """
        Stores a new entity

        Args:
            entity (T): entity to be stored
        """
        raise NotImplementedError("override me")


class BaseRepository(Generic[T], BaseReadRepository[T], BaseWriteRepository[T], metaclass=ABCMeta):
    """
    Base repository
    """
