from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from identity.domain.errors import ValidationException
from identity.domain.validation.validation_handler import ValidationHandler

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class UseCase(Generic[TRequest, TResponse], metaclass=ABCMeta):
    """
    Base class to implement use cases
    """

    validator: ValidationHandler[TRequest]

    @abstractmethod
    def execute(self, request: TRequest) -> TResponse:
        """
        Executes an use case

        Args:
            request (TRequest): represents the request data

        Returns:
            TResponse: returns of the use case
        """
        raise NotImplementedError("override me")

    def validate(self, request: TRequest) -> None:
        """
        Validates a request against a defined validator

        Args:
            request (TRequest): request to validate

        Raises:
            ValidationException: when there are validation errors
        """
        validator: ValidationHandler[TRequest] = getattr(self, "validator", None)

        if not validator:
            return

        errors = validator.validate(request)
        if not errors:
            return

        raise ValidationException(error=errors)
