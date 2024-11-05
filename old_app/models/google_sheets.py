from dataclasses import dataclass
import time

E_MESSAGE_ID = "2PACX-1vT210RbKuZmMqdNkkUBXmDMFg8BsM4mcKloMjhuUME5LXTwFdXt7HeBk5EowEeb4X2_U9Fzei8nzjjk"

@dataclass
class GoogleSheets:
    e_message: str = ""
    
    @staticmethod
    def _google_sheets_url(sheet_id):
        return f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?output=csv&t={int(time.time())}"

    def __post_init__(self):
        self.e_message = self._google_sheets_url(self.e_message)