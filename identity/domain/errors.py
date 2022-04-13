from typing import List, Union

from identity.domain.models.error import ErrorDescription


class LoquiException(Exception):
    """
    Base exception for app exceptions
    """


class AuthException(LoquiException):
    """
    Base exception for handling authentication or authorization errors
    """


class ValidationException(LoquiException):
    errors: List[ErrorDescription]

    def __init__(self, *args, error: Union[ErrorDescription, List[ErrorDescription]], **kwargs) -> None:
        """
        ValidationException constructor

        Args:
            error (Union[ErrorDescription, List[ErrorDescription]]): errors that caused exception
        """
        self.message = "One or more validation errors occurred"
        self.errors = error if isinstance(error, list) else [error]
        super().__init__(*args, **kwargs)
