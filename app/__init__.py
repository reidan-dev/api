from app.models import BaseGoogleSheet, GoogleSheetsHandler
from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import main

    app.register_blueprint(main)

    return app


def create_google_sheet_handlers():
    google_sheets_handler = GoogleSheetsHandler(
        e_message=BaseGoogleSheet("eMessage","An API for the eMessage sheet.", "0"),
    )

    return google_sheets_handler
