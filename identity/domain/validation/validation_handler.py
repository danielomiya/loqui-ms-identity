from typing import Dict, Generic, List

from identity.domain.errors import ErrorDescription
from identity.domain.utils import get_or_init, make_getter
from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import F, T


class ValidationHandler(Generic[T]):
    def __init__(self) -> None:
        self.validations: Dict[str, List[ValidationRule[T, F]]] = {}

    def add(self, field: str, rules: List[ValidationRule[T, F]]) -> "ValidationHandler[T]":
        mapped_rules = [get_or_init(rule) for rule in rules]

        if field in self.validations:
            self.validations += mapped_rules
        else:
            self.validations[field] = mapped_rules

        return self

    def validate(self, o: T) -> List[ErrorDescription]:
        get = make_getter(o)
        acc = []

        for field, rules in self.validations.items():
            for rule in rules:
                err = rule.get_validation_result(get(field), field, o)

                if err:
                    acc.append(ErrorDescription(field=field, message=err))
                    break

        return acc
