from dataclasses import dataclass, field
from typing import Protocol
import requests
import csv
from io import StringIO
from time import time

@dataclass
class BaseAPIProtocol(Protocol):
    pass


@dataclass
class BaseGoogleSheet:
    name: str = ""
    desc: str = ""
    sheet_id: str = ""
    data: dict[str, str | int] = field(default_factory=dict)

    def get_sheet_url(self):
        return f"https://docs.google.com/spreadsheets/d/e/2PACX-1vT210RbKuZmMqdNkkUBXmDMFg8BsM4mcKloMjhuUME5LXTwFdXt7HeBk5EowEeb4X2_U9Fzei8nzjjk/pub?gid={self.sheet_id}&single=true&output=csv"
    
    def get_data(self):
        response = requests.get(self.get_sheet_url())
        response.raise_for_status()
        response.encoding = "utf-8"
        csv_data = csv.DictReader(StringIO(response.text))
        return {row["id"]: row for row in csv_data}

    def __post_init__(self):
        self.data = self.get_data()


@dataclass
class GoogleSheetsHandler:
    e_message: BaseGoogleSheet

    def handler_apis(self):
        return {
            f"/api/goole_sheets/{base_google_sheet.name}" : base_google_sheet.desc
            for _, base_google_sheet in self.__dict__.items()
        }

    def handler_dict(self):
        return {
            base_google_sheet.name : base_google_sheet
            for _, base_google_sheet in self.__dict__.items()
        }