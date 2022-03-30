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
        """
        EitherRule constructor

        Args:
            left (Union[ValidationRule[T, F], Type[ValidationRule[T, F]]]): left rule to test
            right (Union[ValidationRule[T, F], Type[ValidationRule[T, F]]]): right rule to test
            message (str, optional): error message format
                Defaults to "field {0} is not valid for either {1} or {2}"
        """
        self.left: ValidationRule[T, F] = get_or_init(left)
        self.right: ValidationRule[T, F] = get_or_init(right)
        super().__init__(message)

    def is_valid(self, value: F, ctx: T) -> bool:
        """
        Checks if given value is valid conforming to either left or right rule

        Args:
            value (F): input to test
            ctx (T): context of the field

        Returns:
            bool: whether value is valid
        """
        return self.left.is_valid(value, ctx) or self.right.is_valid(value, ctx)

    def format_error(self, name: str) -> str:
        """
        Formats erro rmessage

        Args:
            name (str): name of field

        Returns:
            str: error message
        """
        return self.message.format(name, self.left.__class__.__name__, self.right.__class__.__name__)
