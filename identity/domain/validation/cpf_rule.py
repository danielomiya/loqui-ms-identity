import re
from typing import Generic

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import T


def has_only_repeated_digits(value: str) -> bool:
    return all(value[0] == v for v in value)


class CPFRule(Generic[T], ValidationRule[T, str]):
    def __init__(self, message: str = "field {0} is not a valid CPF") -> None:
        super().__init__(message)

    def is_valid(self, value: str, ctx: T) -> bool:
        if value is None:
            return True

        value = re.sub(r"[^\d]", "", value)

        if len(value) != 11 or has_only_repeated_digits(value):
            return False

        # calc 1st cpf check digit
        sum = 0
        weight = 10

        for n in range(9):
            sum += int(value[n]) * weight
            weight -= 1

        verifying_digit = 11 - sum % 11

        if verifying_digit > 9:
            first_verifying_digit = 0
        else:
            first_verifying_digit = verifying_digit

        # calc 2nd check digit of cpf
        sum = 0
        weight = 11
        for n in range(10):
            sum += int(value[n]) * weight

            # decrement weight
            weight -= 1

        verifying_digit = 11 - sum % 11

        if verifying_digit > 9:
            second_verifying_digit = 0
        else:
            second_verifying_digit = verifying_digit

        return value[-2:] == f"{first_verifying_digit}{second_verifying_digit}"
