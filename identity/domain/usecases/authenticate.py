from typing import TypedDict

from identity.domain.models.token import Token
from identity.domain.usecases.base_use_case import UseCase


class AccessRequestDTO(TypedDict):
    client_id: str
    username: str
    password: str
    scope: str  # = "*"
    grant_type: str  # = "password"


class AuthenticateUseCase(UseCase[AccessRequestDTO, Token]):
    def execute(self, request: AccessRequestDTO) -> Token:
        return super().execute(request)
