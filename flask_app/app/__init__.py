from flask import Flask
from app.routes import user_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix='/users')

    # Swagger UI initialization
    SWAGGER_URL = "/apidoc"
    API_URL = "/static/swagger.json"
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': 'Flask User Resource App'}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app
