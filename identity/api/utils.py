from dataclasses import asdict
from functools import wraps
from http import HTTPStatus
from re import T
from typing import Callable

from identity.domain.errors import ErrorFeedback, ValidationError
from identity.typing import Response


def catch(func: Callable[[], T]) -> Callable[[], T]:
    @wraps(func)
    def wrap(*args, **kwargs) -> Response:
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            if isinstance(ve.error, list):
                errors = ve.error
            else:
                errors = [ve.error]

            feedback = ErrorFeedback(
                title="Validation errors",
                detail="One or more validations have failed",
                status=HTTPStatus.BAD_REQUEST,
                errors=errors,
            )
            return asdict(feedback), feedback.status
        except Exception:
            raise

    return wrap
