from flask import Flask
from identity.api.handlers.user import bp as users_bp


app = Flask(__name__)

app.register_blueprint(users_bp, url_prefix="/api/v1/users")
