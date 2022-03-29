from abc import ABCMeta, abstractmethod
from typing import Generic

from identity.typing import F, T


class ValidationRule(Generic[T, F], metaclass=ABCMeta):
    def __init__(self, message: str = "field {0} is not valid") -> None:
        """
        ValidationRule constructor.

        Args:
            message (str, optional): string to format error messages.
                Defaults to "field {0} is not valid".
        """
        self.message = message

    @abstractmethod
    def is_valid(self, value: F, ctx: T) -> bool:
        """
        Gets whether value is valid.

        Args:
            value (F): value to validate.
            ctx (T): context where value is contained.

        Returns:
            bool: whether valid or not.
        """
        raise NotImplementedError("override me")

    def get_validation_result(self, value: F, field: str, ctx: T = None) -> str:
        """
        Gets the validation result.

        Args:
            value (F): value to be validated.
            field (str): name of the field to format error.
            ctx (T, optional): context where field is contained. Defaults to None.

        Returns:
            str: error message or None.
        """
        result = None

        if not self.is_valid(value, ctx):
            result = self.format_error(field)

        return result

    def format_error(self, name: str) -> str:
        """
        Formats the error message.
        Derived classes can override this method.

        Args:
            name (str): name of the field.

        Returns:
            str: error message.
        """
        return self.message.format(name)
