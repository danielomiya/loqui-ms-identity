from typing import TypedDict

from identity.domain.usecases.base_use_case import UseCase


class ChangePasswordDTO(TypedDict):
    code: str
    new_password: str
    confirm_password: str


class FinishPasswordChangeUseCase(UseCase[ChangePasswordDTO, bool]):
    pass
