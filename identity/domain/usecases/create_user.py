from datetime import datetime
from typing import TypedDict

from identity.domain.errors import ValidationError
from identity.domain.models.user import User
from identity.domain.repositories.user_repository import UserRepository
from identity.domain.services.password_hasher import PasswordHasher
from identity.domain.usecases.base_use_case import UseCase
from identity.domain.validation.confirmation_rule import ConfirmationRule
from identity.domain.validation.contains_rule import ContainsRule
from identity.domain.validation.cpf_rule import CPFRule
from identity.domain.validation.cnpj_rule import CNPJRule
from identity.domain.validation.either_rule import EitherRule
from identity.domain.validation.minimum_age_rule import MinimumAgeRule
from identity.domain.validation.not_empty_rule import NotEmptyRule


class CreateUserDTO(TypedDict):
    name: str
    document: str
    birth_date: datetime
    email: str
    phone: str
    password: str
    confirm_password: str
    picture_url: str


class CreateUserUseCase(UseCase[CreateUserDTO, User]):
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, request: CreateUserDTO) -> User:
        validator = ContainsRule(
            "name",
            "document",
            "birth_date",
            "email",
            "password",
            "confirm_password",
        )
        (
            validator.next(NotEmptyRule("name"))
            .next(NotEmptyRule("document"))
            .next(NotEmptyRule("birth_date"))
            .next(NotEmptyRule("email"))
            .next(ConfirmationRule("password", "confirm_password"))
            .next(EitherRule(CPFRule("document"), CNPJRule("document")))
            .next(MinimumAgeRule("birth_date", 18))
        )

        err = validator.handle(request)
        if err:
            raise ValidationError(error=err)

        hashed_password = self.password_hasher.hash(request["password"])

        for key in ("password", "confirm_password"):
            # user entity doesn't contain these keys
            request.pop(key)

        user = User(id=0, **request, hashed_password=hashed_password)
        self.user_repository.store(user)
        return user
