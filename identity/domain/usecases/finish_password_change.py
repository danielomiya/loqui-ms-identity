from dataclasses import dataclass

from identity.domain.usecases.base_use_case import UseCase


@dataclass
class ChangePasswordDTO:
    code: str
    new_password: str
    confirm_password: str


class FinishPasswordChangeUseCase(UseCase[ChangePasswordDTO, bool]):
    pass
