from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@main.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}
    return jsonify(data)
