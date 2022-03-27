from typing import TypedDict
from identity.domain.models.token import Token
from identity.domain.usecases.base_use_case import UseCase


class RefreshTokenDTO(TypedDict):
    client_id: int
    refresh_token: str
    scope: str  # = "*"
    grant_type: str  # = "refresh_token"


class RefreshTokenUseCase(UseCase[RefreshTokenDTO, Token]):
    def execute(self, request: RefreshTokenDTO) -> Token:
        return super().execute(request)
