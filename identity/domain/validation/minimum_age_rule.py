from datetime import datetime
from typing import Callable

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import T


class MinimumAgeRule(ValidationRule[T, datetime]):
    def __init__(
        self,
        min_age: int,
        now: Callable[[], datetime] = datetime.utcnow,
        message: str = "field {0} not old enough to be {1} year old",
    ) -> None:
        self.min_age = min_age
        self.now = now
        super().__init__(message)

    def is_valid(self, value: datetime, ctx: T) -> bool:
        if value is None:
            return True

        timespan = self.now() - value
        total_years = timespan.days / 365.25

        if total_years < self.min_age:
            return False

        return True

    def format_error(self, name: str) -> str:
        """
        Formats the error message.

        Args:
            name (str): name of the field.

        Returns:
            str: error message.
        """
        return self.message.format(name, self.min_age)
