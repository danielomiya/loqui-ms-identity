from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class UseCase(Generic[TRequest, TResponse], metaclass=ABCMeta):
    @abstractmethod
    def execute(self, request: TRequest) -> TResponse:
        raise NotImplementedError("override me")
