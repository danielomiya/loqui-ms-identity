from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from identity.domain.errors import ErrorDescription
from identity.typing import JSON

T = TypeVar("T")


class ValidationHandler(Generic[T]):
    _next: "ValidationHandler" = None

    def next(self, handler: "ValidationHandler") -> "ValidationHandler":
        self._next = handler
        return handler

    def handle(self, value: T) -> ErrorDescription:
        if hasattr(self, "validate"):
            result = self.validate(value)

            if result is not None:
                return result

        if self._next:
            return self._next.handle(value)

        return None


class JSONValidationHandler(ValidationHandler[JSON], metaclass=ABCMeta):
    def __init__(self, field: str) -> None:
        self.field = field

    @abstractmethod
    def validate(self, json: JSON) -> ErrorDescription:
        raise NotImplementedError("override me")
