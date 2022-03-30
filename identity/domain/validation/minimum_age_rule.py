from datetime import datetime
from typing import Callable, Union

from identity.domain.validation.validation_rule import ValidationRule
from identity.typing import T


class MinimumAgeRule(ValidationRule[T, datetime]):
    def __init__(
        self,
        min_age: int,
        reference_date: Union[datetime, Callable[[], datetime]] = datetime.utcnow,
        message: str = "field {0} not old enough to be {1} year old",
    ) -> None:
        """
        MinimumAgeRule constructor

        Args:
            min_age (int): minimum age
            reference_date (Union[datetime, Callable[[], datetime]], optional): function to get reference
                datetime (avoid side effects). Defaults to datetime.utcnow
            message (str, optional): error message format
                Defaults to "field {0} not old enough to be {1} year old"
        """
        self.min_age = min_age
        self.reference_date = reference_date
        super().__init__(message)

    def is_valid(self, value: datetime, ctx: T) -> bool:
        if value is None:
            return True

        date = self.reference_date() if callable(self.reference_date) else self.reference_date
        timespan = date - value
        total_years = timespan.days / 365.25

        return total_years >= self.min_age

    def format_error(self, name: str) -> str:
        """
        Formats the error message

        Args:
            name (str): name of the field

        Returns:
            str: error message
        """
        return self.message.format(name, self.min_age)
