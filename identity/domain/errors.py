from dataclasses import dataclass, field
from math import factorial
from typing import List


@dataclass
class ErrorDescription:
    field: str
    message: str


@dataclass
class ErrorFeedback:
    title: str
    detail: str
    status: int
    type: str = None
    errors: List[ErrorDescription] = field(default_factory=list)


class LoquiException(BaseException):
    pass


class ValidationError(LoquiException):
    error: ErrorDescription

    def __init__(
        self, *args, error: ErrorFeedback | ErrorDescription, **kwargs
    ) -> None:
        self.error = error
        super().__init__(*args, **kwargs)
