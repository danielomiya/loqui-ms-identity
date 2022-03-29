from typing import Generic

from identity.domain.utils import make_getter
from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import F, T


class ConfirmationRule(Generic[T, F], ValidationRule[T, F]):
    def __init__(
        self,
        field: str,
        message: str = "field {0} is not equal to {1}",
    ) -> None:
        """
        ConfirmationRule constructor.

        Args:
            field (str): field to compare (must be available in ctx)
            message (str, optional): error message format. Defaults to "field {0} is not equal to {1}".
        """
        self.field = field
        super().__init__(message)

    def is_valid(self, value: F, ctx: T = None) -> bool:
        get = make_getter(ctx)
        return value == get(self.field)
