from dataclasses import dataclass, field
from typing import List


@dataclass
class ErrorDescription:
    """
    Represents a localized error description
    """

    field: str  # field where error happened
    message: str  # error message


@dataclass
class ErrorFeedback:
    """
    Represents a complete error feedback
    """

    title: str  # common title of the feedback
    detail: str  # detailed description
    status: int  # status (generally HTTP status)
    type: str = None  # link to the documentation of the error (if any)
    errors: List[ErrorDescription] = field(default_factory=list)  # list of errors per field
