# 📘 Member Directory App

A lightweight, searchable member directory web app built with [Streamlit](https://streamlit.io/) and backed by Google Sheets. Designed for organizations with up to a few hundred members who want an easy-to-maintain, fully customized UI without the overhead of enterprise platforms.

---

## 🚀 Features

* 🔍 Filter members by name or department
* 👤 View individual member details
* 🗒️ Data stored and managed in Google Sheets
* 🔐 Admin-only editing support (optional)
* ⚡ Fast deployment via Streamlit Cloud or any Python host



---

## 🏧 Project Structure

```
member-directory-app/
├── app/
│   └── streamlit_app.py       # Main application
├── .env                       # Contains Google Sheet ID and secrets
├── service_account.json       # Google API credentials (not tracked in Git)
├── pyproject.toml             # Project metadata and dependencies
├── .gitignore
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/member-directory-app.git
cd member-directory-app
```

### 2. Set up Python environment (using [uv](https://github.com/astral-sh/uv))

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt  # or install from pyproject.toml
```

### 3. Configure `.env`

Create a `.env` file:

```
GOOGLE_SHEET_ID=your_google_sheet_id
SERVICE_ACCOUNT=service_account.json
```

### 4. Add Google Service Account

* Generate a `service_account.json` from Google Cloud Console
* Place it in the root folder
* Share the target Google Sheet with the service account's email address (as editor)

---

## 🧪 Run the App

```bash
streamlit run app/streamlit_app.py
```

The app will launch at `http://localhost:8501`

### Demo page

If you just want to see a simple list of members, run:

```bash
streamlit run app/demo.py
```

---

## 🌐 Deployment

For easy hosting, use:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Render](https://render.com/)
* [Google Cloud Run](https://cloud.google.com/run)

> Streamlit Cloud supports Google login, secrets management, and continuous deployment from GitHub.

---

## 🔒 Environment Variables

| Variable          | Description                             |
| ----------------- | --------------------------------------- |
| `GOOGLE_SHEET_ID` | ID of the Google Sheet (from its URL)   |
| `ADMIN_EMAILS`    | (Optional) Comma-separated admin emails |
| `SERVICE_ACCOUNT` | JSON credentials file (local path)      |

---

## 📌 Roadmap Ideas

* [ ] Admin login + write access
* [ ] Member profile pictures (from Drive or URL)
* [ ] Form to add/edit/delete members
* [ ] Department view page

---

## 📄 License

MIT License. Built by [Tiana Smith](https://github.com/YOUR_USERNAME).
