from dataclasses import asdict, dataclass
from datetime import datetime

from identity.domain.errors import ValidationException
from identity.domain.models.user import User
from identity.domain.repositories.user_repository import UserRepository
from identity.domain.services.password_hasher import PasswordHasher
from identity.domain.usecases.base_use_case import UseCase
from identity.domain.validation.cnpj_rule import CNPJRule
from identity.domain.validation.confirmation_rule import ConfirmationRule
from identity.domain.validation.cpf_rule import CPFRule
from identity.domain.validation.either_rule import EitherRule
from identity.domain.validation.minimum_age_rule import MinimumAgeRule
from identity.domain.validation.not_empty_rule import NotEmptyRule
from identity.domain.validation.required_rule import RequiredRule
from identity.domain.validation.validation_handler import ValidationHandler


@dataclass
class CreateUserDTO:
    name: str
    document: str
    birth_date: datetime
    email: str
    password: str
    confirm_password: str
    phone: str = None
    picture_url: str = None


class CreateUserUseCase(UseCase[CreateUserDTO, User]):
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, request: CreateUserDTO) -> User:
        validator = (
            ValidationHandler[CreateUserDTO]()
            .add("name", [RequiredRule, NotEmptyRule])
            .add("document", [RequiredRule, NotEmptyRule, EitherRule(CPFRule, CNPJRule)])
            .add("birth_date", [RequiredRule, MinimumAgeRule(18)])
            .add("email", [RequiredRule, NotEmptyRule])
            .add("password", [RequiredRule])
            .add("confirm_password", [RequiredRule, ConfirmationRule("password")])
        )

        errors = validator.validate(request)
        if errors:
            raise ValidationException(error=errors)

        hashed_password = self.password_hasher.hash(request.password)

        entity = asdict(request)
        for key in ("password", "confirm_password"):
            # user entity doesn't contain these keys
            entity.pop(key)

        user = User(id=0, hashed_password=hashed_password, **entity)
        self.user_repository.store(user)

        return user
