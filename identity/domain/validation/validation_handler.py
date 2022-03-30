from typing import Dict, Generic, List

from identity.domain.models.error import ErrorDescription
from identity.domain.utils import get_or_init, make_getter
from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import F, T


class ValidationHandler(Generic[T]):
    def __init__(self) -> None:
        """
        ValidationHandler constructor
        """
        self.validations: Dict[str, List[ValidationRule[T, F]]] = {}

    def add(self, field: str, rules: List[ValidationRule[T, F]]) -> "ValidationHandler[T]":
        """
        Adds a rule to given field

        Args:
            field (str): name of the field
            rules (List[ValidationRule[T, F]]): rules to add

        Returns:
            ValidationHandler[T]: this instance
        """
        mapped_rules = [get_or_init(rule) for rule in rules]

        if field in self.validations:
            self.validations += mapped_rules
        else:
            self.validations[field] = mapped_rules

        return self

    def validate(self, o: T) -> List[ErrorDescription]:
        """
        Validates given object against configured constraints

        Args:
            o (T): object to test

        Returns:
            List[ErrorDescription]: list of errors
        """
        get = make_getter(o)
        acc = []

        for field, rules in self.validations.items():
            for rule in rules:
                err = rule.get_validation_result(get(field), field, o)

                if err:
                    acc.append(ErrorDescription(field=field, message=err))
                    break

        return acc
