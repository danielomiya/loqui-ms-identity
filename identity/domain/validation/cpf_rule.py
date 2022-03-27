import re

from identity.domain.errors import ErrorDescription
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


def has_only_repeated_digits(value: str) -> bool:
    return all(value[0] == v for v in value)


class CPFRule(JSONValidationHandler):
    def validate(self, json: JSON) -> ErrorDescription:
        o = json.get(self.field)
        error = ErrorDescription(
            field=self.field,
            message=f"Field {self.field} is not a valid CPF",
        )

        if not o:
            return None

        value = re.sub(r"[^\d]", "", o)

        if len(value) != 11 or has_only_repeated_digits(value):
            return error

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

        if value[-2:] != f"{first_verifying_digit}{second_verifying_digit}":
            return error

        return None
