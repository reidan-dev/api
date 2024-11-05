from app import create_google_sheet_handlers
from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

google_sheets_handler = create_google_sheet_handlers()

NOT_FOUND = {"ERROR" : "API NOT FOUND!"}

@main.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@main.route("/api/google_sheets", methods=["GET"])
def get_google_sheets():
    return jsonify(google_sheets_handler.handler_apis())

@main.route("/api/google_sheets/<string:sheet_name>", methods=['GET'])
def get_google_sheet(sheet_name: str):
    gs_dict = google_sheets_handler.handler_dict()
    if sheet_name not in gs_dict:
        return jsonify(NOT_FOUND)
    return gs_dict[sheet_name].get_data()