from dataclasses import asdict
from datetime import datetime
from http import HTTPStatus

from dacite import Config, from_dict
from flask import Blueprint, request

from identity.domain.usecases.create_user import CreateUserDTO, CreateUserUseCase
from identity.domain.utils import parse_iso_datetime
from identity.typing import Response
from identity.users.repositories.sqlalchemy.user_repository import UserRepository
from identity.users.services.bcrypt_service import BcryptService

bp = Blueprint("users", __name__)

user_repository = UserRepository()
bcrypt_service = BcryptService()
create_user_use_case = CreateUserUseCase(
    user_repository,
    password_hasher=bcrypt_service,
)


@bp.post("/")
def create_user() -> Response:
    body = request.get_json()
    dto = from_dict(CreateUserDTO, body, Config(type_hooks={datetime: parse_iso_datetime}))
    user = create_user_use_case.execute(dto)
    return asdict(user), HTTPStatus.CREATED


@bp.get("/<int:id>")
def get_user(id: int) -> None:
    pass


@bp.get("/me")
def get_me() -> None:
    pass
