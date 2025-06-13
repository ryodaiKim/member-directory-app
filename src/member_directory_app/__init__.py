"""Utilities for the member directory app."""

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "members.csv"


def load_members() -> pd.DataFrame:
    """Load member data from the local CSV file.

    Returns
    -------
    pandas.DataFrame
        Table of members.
    """
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame(columns=["Name", "Department", "Email"])


def hello() -> str:
    """Sample helper to ensure package import works."""
    return "Hello from member-directory-app!"
