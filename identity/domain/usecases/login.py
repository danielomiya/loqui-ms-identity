from typing import TypedDict

from identity.domain.usecases.base_use_case import UseCase


class LoginDTO(TypedDict):
    email: str
    password: str


class LoginUseCase(UseCase[LoginDTO, bool]):
    pass
