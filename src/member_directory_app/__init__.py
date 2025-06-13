"""Utilities for the member directory app."""

from pathlib import Path
import os
import pandas as pd
import gspread
from google.oauth2 import service_account

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "members.csv"


def _load_from_google_sheet(sheet_id: str, credentials_path: str) -> pd.DataFrame:
    """Fetch member records from a Google Sheet.

    Parameters
    ----------
    sheet_id:
        The ID of the Google Sheet.
    credentials_path:
        Path to a service account JSON credentials file.

    Returns
    -------
    pandas.DataFrame
        Data from the first worksheet of the sheet.
    """
    creds = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.sheet1
    records = worksheet.get_all_records()
    return pd.DataFrame(records)


def load_members() -> pd.DataFrame:
    """Load member data from Google Sheets if configured, otherwise from CSV."""
    sheet_id = os.getenv("GOOGLE_SHEET_ID")
    service_account_path = os.getenv("SERVICE_ACCOUNT", "service_account.json")

    if sheet_id and Path(service_account_path).exists():
        try:
            return _load_from_google_sheet(sheet_id, service_account_path)
        except Exception as exc:  # pragma: no cover - network dependency
            print(f"Failed to load Google Sheet: {exc}")

    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    return pd.DataFrame(columns=["Name", "Department", "Email"])


def hello() -> str:
    """Sample helper to ensure package import works."""
    return "Hello from member-directory-app!"
