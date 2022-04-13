from dataclasses import dataclass

from identity.domain.usecases.authenticate import TokenDTO
from identity.domain.usecases.base_use_case import UseCase


@dataclass
class RefreshTokenDTO:
    client_id: int
    refresh_token: str
    scope: str  # = "*"
    grant_type: str  # = "refresh_token"


class RefreshTokenUseCase(UseCase[RefreshTokenDTO, TokenDTO]):
    def execute(self, request: RefreshTokenDTO) -> TokenDTO:
        return super().execute(request)
