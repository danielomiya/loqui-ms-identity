import re

from identity.domain.errors import ErrorDescription
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


def has_only_repeated_digits(value: str) -> bool:
    return all(value[0] == v for v in value)


class CNPJRule(JSONValidationHandler):
    def validate(self, json: JSON) -> ErrorDescription:
        o = json.get(self.field)
        error = ErrorDescription(
            field=self.field,
            message=f"Field {self.field} is not a valid CNPJ valid",
        )

        if not o:
            return None

        value = re.sub(r"[^\d]", "", o)

        if len(value) != 14 or has_only_repeated_digits(value):
            return error

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

        if value[-2:] != f"{first_verifying_digit}{second_verifying_digit}":
            return error

        return None
