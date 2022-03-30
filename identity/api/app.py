from flask import Flask

from identity.api.handlers.errors import handle_validation_error
from identity.api.handlers.user import bp as users_bp
from identity.api.serde.json_serializer import JSONSerializer
from identity.domain.errors import ValidationError

app = Flask(__name__)
app.json_encoder = JSONSerializer

app.register_blueprint(users_bp, url_prefix="/api/v1/users")
app.register_error_handler(ValidationError, handle_validation_error)
