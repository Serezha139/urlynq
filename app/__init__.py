from flask import Flask

from app.routes import main


def create_app():
    from services.mongo_vectorization import vectorization_service   # initializing it here
    app = Flask(__name__)
    app.register_blueprint(main)
    return app


app = create_app()
