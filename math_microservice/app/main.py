from flask import Flask
from app.controllers.math_controller import math_bp
from app.db import init_db
from app.config import Config

from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    app.register_blueprint(math_bp, url_prefix='/api/math')

    # Swagger/OpenAPI template cu Bearer Token
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Math Microservice API",
            "description": "API pentru operații matematice cu autorizare Bearer Token.",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Introdu tokenul în formatul: Bearer <token>"
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }

    Swagger(app, template=swagger_template)

    @app.route('/')
    def root():
        return {"message": "Math Microservice API is running! Go to /apidocs for endpoint documentation."}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
