from identity.domain.errors import ErrorDescription
from identity.domain.validation.base import JSONValidationHandler
from identity.typing import JSON


class ContainsRule(JSONValidationHandler):
    def __init__(self, *fields: str) -> None:
        super().__init__("*")
        self.fields = set(fields)

    def validate(self, json: JSON) -> ErrorDescription:
        missing = self.fields - set(json.keys())

        if not missing:
            return None

        return ErrorDescription(
            field=self.field,
            message=f"JSON doesn't contain fields: {', '.join(missing)}",
        )
