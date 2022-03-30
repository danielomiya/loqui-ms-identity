from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class UseCase(Generic[TRequest, TResponse], metaclass=ABCMeta):
    """
    Base class to implement use cases
    """

    @abstractmethod
    def execute(self, request: TRequest) -> TResponse:
        """
        Executes an use case

        Args:
            request (TRequest): represents the request data

        Returns:
            TResponse: returns of the use case
        """
        raise NotImplementedError("override me")
