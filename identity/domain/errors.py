from typing import List, Union

from identity.domain.models.error import ErrorDescription


class LoquiException(Exception):
    """
    Base exception for app exceptions
    """


class ValidationError(LoquiException):
    errors: List[ErrorDescription]

    def __init__(self, *args, error: Union[ErrorDescription, List[ErrorDescription]], **kwargs) -> None:
        """
        ValidationError constructor

        Args:
            error (Union[ErrorDescription, List[ErrorDescription]]): errors that caused exception
        """
        self.errors = error if isinstance(error, list) else [error]
        super().__init__(*args, **kwargs)
