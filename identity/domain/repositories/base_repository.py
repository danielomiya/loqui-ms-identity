from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseReadRepository(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id: int) -> T:
        raise NotImplementedError("override me")


class BaseWriteRepository(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def store(self, entity: T) -> None:
        raise NotImplementedError("override me")


class BaseRepository(Generic[T], BaseReadRepository[T], BaseWriteRepository[T], metaclass=ABCMeta):
    pass
