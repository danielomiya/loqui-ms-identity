from dataclasses import dataclass

from identity.domain.models.token import Token
from identity.domain.usecases.base_use_case import UseCase


@dataclass
class RefreshTokenDTO:
    client_id: int
    refresh_token: str
    scope: str  # = "*"
    grant_type: str  # = "refresh_token"


class RefreshTokenUseCase(UseCase[RefreshTokenDTO, Token]):
    def execute(self, request: RefreshTokenDTO) -> Token:
        return super().execute(request)
