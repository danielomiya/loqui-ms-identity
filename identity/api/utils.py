from dataclasses import asdict
from functools import wraps
from http import HTTPStatus

from identity.domain.errors import ErrorFeedback, ValidationError
from identity.typing import Response


def catch(func: callable) -> callable:
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
