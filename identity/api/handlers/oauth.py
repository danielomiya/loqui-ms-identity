from http import HTTPStatus

from dacite import from_dict
from flask import request
from flask.blueprints import Blueprint

from identity.domain.usecases.authenticate import AccessRequestDTO, AuthenticateUseCase

bp = Blueprint("oauth", __name__)

authenticate_use_case = AuthenticateUseCase()


@bp.post("/token")
def get_token():
    dto = from_dict(data_class=AccessRequestDTO, data=request.form)
    token = authenticate_use_case.execute(dto)
    return token, HTTPStatus.OK
