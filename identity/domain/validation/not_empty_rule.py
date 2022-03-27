from identity.domain.errors import ErrorDescription
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


class NotEmptyRule(JSONValidationHandler):
    def validate(self, json: JSON) -> ErrorDescription:
        o = json.get(self.field)

        if o and len(o):
            return None

        return ErrorDescription(
            field=self.field,
            message=f"Field {self.field} must be not empty",
        )
