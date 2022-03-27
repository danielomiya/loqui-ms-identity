from typing import TypedDict

from identity.domain.usecases.base_use_case import UseCase


class RequestPasswordChangeDTO(TypedDict):
    email: str


class StartPasswordChangeUseCase(UseCase[RequestPasswordChangeDTO, None]):
    pass
