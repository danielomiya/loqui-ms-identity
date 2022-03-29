from flask import Flask

from identity.api.handlers.user import bp as users_bp
from identity.api.serde.json_serializer import JSONSerializer

app = Flask(__name__)
app.json_encoder = JSONSerializer

app.register_blueprint(users_bp, url_prefix="/api/v1/users")
