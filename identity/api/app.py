from flask import Flask
from flask_cors import CORS

from identity.api.handlers.errors import handle_validation_error
from identity.api.handlers.user import bp as users_bp
from identity.api.serde.json_serializer import JSONSerializer
from identity.domain.errors import ValidationException

app = Flask(__name__)
app.json_encoder = JSONSerializer
CORS(app)

app.register_blueprint(users_bp, url_prefix="/api/v1/users")
app.register_error_handler(ValidationException, handle_validation_error)
