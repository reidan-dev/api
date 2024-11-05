import csv
from io import StringIO
from old_app.models.google_sheets import E_MESSAGE_ID, GoogleSheets
import requests
from flask import Flask, jsonify, request


def main():

    # google_sheets_handler = GoogleSheets(
    #     e_message=E_MESSAGE_ID
    # )

    # # Fetch the CSV data
    # response = requests.get(google_sheets_handler.e_message)
    # response.raise_for_status()  # Check for any errors

    # # Specify the correct encoding (usually UTF-8, but you can adjust if needed)
    # response.encoding = 'utf-8'

    # # Use csv.DictReader to parse the data
    # csv_data = csv.DictReader(StringIO(response.text))

    # # Convert the data to a list of dictionaries
    # data = [row for row in csv_data]

    # for row in data:
    #     print(row)
