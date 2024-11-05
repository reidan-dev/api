from flask import Flask
from flask_cors import CORS

from app.models import BaseGoogleSheet, GoogleSheetsHandler

from .config import Config


def create_app():
    app = Flask(__name__)
    # Enable CORS for all routes
    # CORS(app, resources={r"/api/*": {"origins": ["https://e-message.vercel.app/"]}})
    CORS(app)



    # Optionally, you can specify which origins are allowed
    # CORS(app, resources={r"/api/*": {"origins": "https://your-allowed-origin.com"}})

    app.config.from_object(Config)

    from .routes import main

    app.register_blueprint(main)

    return app


def create_google_sheet_handlers():
    google_sheets_handler = GoogleSheetsHandler(
        e_message=BaseGoogleSheet("eMessage", "An API for the eMessage sheet.", "0"),
    )

    return google_sheets_handler
