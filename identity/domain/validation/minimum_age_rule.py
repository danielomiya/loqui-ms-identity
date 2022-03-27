from datetime import datetime
from typing import Callable

from identity.domain.errors import ErrorDescription
from identity.domain.utils import parse_iso_datetime
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


class MinimumAgeRule(JSONValidationHandler):
    def __init__(
        self, field: str, min_age: int, now: Callable[[], datetime] = datetime.utcnow
    ) -> None:
        self.min_age = min_age
        self.now = now
        super().__init__(field)

    def validate(self, json: JSON) -> ErrorDescription:
        o = json.get(self.field)
        if not o:
            return None

        dttm_point = parse_iso_datetime(o)
        timespan = self.now() - dttm_point
        total_years = timespan.days / 365.25

        if total_years >= self.min_age:
            return None

        return ErrorDescription(
            field=self.field,
            message=f"Field {self.field} not old enough to be {self.min_age} year old",
        )
