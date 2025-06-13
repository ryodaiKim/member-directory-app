from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from . import load_members


def main(argv: list[str] | None = None) -> None:
    """Entry point for the member directory CLI."""
    parser = argparse.ArgumentParser(description="Member Directory CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser(
        "load-sheet", help="Load member data from Google Sheets and print as CSV"
    )
    subparsers.add_parser(
        "demo", help="Launch the Streamlit demo page listing members"
    )

    args = parser.parse_args(argv)

    if args.command == "load-sheet":
        df = load_members()
        if df.empty:
            print("No member data found.")
        else:
            print(df.to_csv(index=False))
    elif args.command == "demo":
        demo_path = Path(__file__).resolve().parents[1] / "app" / "demo.py"
        subprocess.run(["streamlit", "run", str(demo_path)], check=False)


if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
