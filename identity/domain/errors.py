from dataclasses import dataclass, field
from typing import List, Union


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
    error: Union[ErrorDescription, List[ErrorDescription]]

    def __init__(self, *args, error: Union[ErrorDescription, List[ErrorDescription]], **kwargs) -> None:
        self.error = error
        super().__init__(*args, **kwargs)
