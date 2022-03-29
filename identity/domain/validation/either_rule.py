from typing import Generic, Type, Union

from identity.domain.utils import get_or_init
from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import F, T


class EitherRule(Generic[T, F], ValidationRule[T, F]):
    def __init__(
        self,
        left: Union[ValidationRule[T, F], Type[ValidationRule[T, F]]],
        right: Union[ValidationRule[T, F], Type[ValidationRule[T, F]]],
        message: str = "field {0} is not valid for either {1} or {2}",
    ) -> None:
        self.left: ValidationRule[T, F] = get_or_init(left)
        self.right: ValidationRule[T, F] = get_or_init(right)
        super().__init__(message)

    def is_valid(self, value: F, ctx: T) -> bool:
        return self.left.is_valid(value, ctx) or self.right.is_valid(value, ctx)

    def format_error(self, name: str) -> str:
        return self.message.format(name, self.left.__class__.__name__, self.left.__class__.__name__)
