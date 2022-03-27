from typing import TypeVar
from identity.domain.validation.base import ValidationHandler
from identity.domain.errors import ErrorDescription


T = TypeVar("T")


class EitherRule(ValidationHandler[T]):
    def __init__(self, left: ValidationHandler[T], right: ValidationHandler[T]) -> None:
        self.left = left
        self.right = right

    def validate(self, o: T) -> ErrorDescription:
        err = self.left.handle(o)

        if err and not self.right.handle(o):
            return None
        return err
