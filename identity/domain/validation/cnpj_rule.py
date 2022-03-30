import re
from typing import Generic

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import T


def has_only_repeated_digits(value: str) -> bool:
    return all(value[0] == v for v in value)


class CNPJRule(Generic[T], ValidationRule[T, str]):
    def __init__(self, message="field {0} is not a valid CNPJ valid") -> None:
        """
        CNPJRule constructor

        Args:
            message (str, optional): error message format
                Defaults to "field {0} is not a valid CNPJ valid"
        """
        self.message = message

    def is_valid(self, value: str, ctx: T) -> bool:
        """
        Checks if given value is a valid CNPJ

        Args:
            value (str): CNPJ value to test
            ctx (T): context of field

        Returns:
            bool: whether value is valid or not
        """
        if not value:
            return True

        value = re.sub(r"[^\d]", "", value)

        if len(value) != 14 or has_only_repeated_digits(value):
            return False

        sum = 0
        weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # calc the 1st cnpj check digit
        for n in range(12):
            value = int(value[n]) * weight[n]
            sum += value

        verifying_digit = sum % 11

        if verifying_digit < 2:
            first_verifying_digit = 0
        else:
            first_verifying_digit = 11 - verifying_digit

        # calc the second check digit of cnpj
        sum = 0
        weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        for n in range(13):
            sum += int(value[n]) * weight[n]

        verifying_digit = sum % 11

        if verifying_digit < 2:
            second_verifying_digit = 0
        else:
            second_verifying_digit = 11 - verifying_digit

        return value[-2:] == f"{first_verifying_digit}{second_verifying_digit}"
