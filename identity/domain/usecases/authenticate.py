from dataclasses import dataclass
from datetime import timedelta

from identity.domain.errors import AuthException
from identity.domain.repositories.access_token_repository import AccessTokenRepository
from identity.domain.repositories.client_repository import ClientRepository
from identity.domain.repositories.refresh_token_repository import RefreshTokenRepository
from identity.domain.repositories.user_repository import UserRepository
from identity.domain.services.password_comparer import PasswordComparer
from identity.domain.services.token_encoder import TokenEncoder
from identity.domain.usecases.base_use_case import UseCase
from identity.domain.validation.required_rule import RequiredRule
from identity.domain.validation.validation_handler import ValidationHandler


@dataclass
class AccessRequestDTO:
    client_id: str
    username: str
    password: str
    scope: str  # = "*"
    grant_type: str  # = "password"


@dataclass
class TokenDTO:
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str = "Bearer"
    scope: str = "*"


class AuthenticateUseCase(UseCase[AccessRequestDTO, TokenDTO]):
    def __init__(
        self,
        user_repository: UserRepository,
        client_repository: ClientRepository,
        access_token_repository: AccessTokenRepository,
        refresh_token_repository: RefreshTokenRepository,
        password_comparer: PasswordComparer,
        token_encoder: TokenEncoder,
    ) -> None:
        self.user_repository = user_repository
        self.client_repository = client_repository
        self.access_token_repository = access_token_repository
        self.refresh_token_repository = refresh_token_repository
        self.password_comparer = password_comparer
        self.token_encoder = token_encoder

        self.validator = (
            ValidationHandler[AccessRequestDTO]()
            .add("client_id", [RequiredRule])
            .add("username", [RequiredRule])
            .add("password", [RequiredRule])
            .add("scope", [RequiredRule])
            .add("grant_type", [RequiredRule])
        )

    def execute(self, request: AccessRequestDTO) -> TokenDTO:
        self.validate(request)

        client = self.client_repository.get_by_id(request.client_id)
        if not client:
            raise AuthException("client is not eligible")

        user = self.user_repository.get_by_email(request.username)
        if not user or not self.password_comparer.compare(request.password, user.hashed_password):
            raise AuthException("wrong username or password")

        expires_in = timedelta(hours=1).total_seconds()

        token = self.token_encoder.encode(
            {
                "iss": "ms-identity",
                "aud": client.id,
                "sub": user.id,
                "exp": expires_in,
            }
        )

        # TODO: implement persistance of issued tokens
        # self.access_token_repository.store(AccessToken())
        # self.refresh_token_repository.store(RefreshTokenRepository())

        return TokenDTO(
            access_token=token,
            refresh_token="",
            expires_in=expires_in,
            token_type="Bearer",
            scope="*",
        )
