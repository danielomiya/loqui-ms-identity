from identity.domain.errors import ErrorDescription
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


class ConfirmationRule(JSONValidationHandler):
    def __init__(self, field: str, field_to_compare: str) -> None:
        super().__init__(field)
        self.field_to_compare = field_to_compare

    def validate(self, json: JSON) -> ErrorDescription:
        o1, o2 = json.get(self.field), json.get(self.field_to_compare)

        if o1 == o2:
            return None

        return ErrorDescription(
            field=self.field,
            message=f"Field {self.field} is not equal to {self.field_to_compare}",
        )
