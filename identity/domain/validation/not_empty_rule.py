from typing import Sized

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import T


class NotEmptyRule(ValidationRule[T, Sized]):
    def __init__(self, message: str = "field {0} must be not empty") -> None:
        super().__init__(message)

    def is_valid(self, value: Sized, ctx: T) -> bool:
        return bool(value is None or len(value))
