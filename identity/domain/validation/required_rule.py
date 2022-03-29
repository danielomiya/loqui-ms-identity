from typing import Generic

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import F, T


class RequiredRule(Generic[T, F], ValidationRule[T, F]):
    def __init__(self, message: str = "field {0} is required") -> None:
        super().__init__(message)

    def is_valid(self, value: F, ctx: T) -> bool:
        return value is not None
