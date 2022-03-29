from dataclasses import dataclass

from identity.domain.usecases.base_use_case import UseCase


@dataclass
class RequestPasswordChangeDTO:
    email: str


class StartPasswordChangeUseCase(UseCase[RequestPasswordChangeDTO, None]):
    pass
