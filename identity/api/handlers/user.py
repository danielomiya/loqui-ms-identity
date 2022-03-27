from dataclasses import asdict
from functools import wraps
from http import HTTPStatus

from flask import Blueprint, request
from identity.domain.errors import (
    ErrorFeedback,
    LoquiException,
    ValidationError,
)
from identity.domain.usecases.create_user import CreateUserUseCase
from identity.users.repositories.sqlalchemy.user_repository import UserRepository
from identity.users.services.bcrypt_service import BcryptService

bp = Blueprint("users", __name__)

user_repository = UserRepository()
bcrypt_service = BcryptService()
create_user_use_case = CreateUserUseCase(
    user_repository,
    password_hasher=bcrypt_service,
)


def catch(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            feedback = ErrorFeedback(
                title="Validation errors",
                detail="One or more validations have failed",
                status=HTTPStatus.BAD_REQUEST,
                errors=[ve.error],
            )
            return asdict(feedback), feedback.status
        except Exception:
            raise

    return wrap


@bp.post("/")
@catch
def create_user() -> None:
    body = request.get_json()
    create_user_use_case.execute(body)


@bp.get("/<int:id>")
def get_user(id: int) -> None:
    pass


@bp.get("/me")
def get_me() -> None:
    pass
