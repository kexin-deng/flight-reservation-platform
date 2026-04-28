# Flight Reservation Platform

A full-stack web application for airline ticket booking, supporting customers, booking agents, and airline staff.

## Features
- User login and registration
- Flight search and booking
- Role-based access (customer, agent, staff)
- Database-backed reservation system

## Tech Stack
- Python (Flask)
- MySQL
- HTML / CSS / JavaScript

## How to Run Locally
```bash
pip install -r requirements.txt
python app/main.py
```

The local app runs at `http://127.0.0.1:8000`.

By default, the app connects to a local MySQL database using:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=final_project_3
```

You can override those values with environment variables.

## Render Deployment

This project is ready for Render's free web service tier. Render does not provide a free MySQL database, so use an external MySQL provider and put those connection values into Render environment variables.

1. Push this repository to GitHub.
2. Create or restore your MySQL database with the schema and data for `final_project_3` on a cloud MySQL provider.
3. In Render, click **New +** > **Web Service**.
4. Connect the GitHub repository.
5. Use these settings:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.main:app --bind 0.0.0.0:${PORT:-8000}`
   - **Instance Type**: `Free`
6. Add these Render environment variables:
   - `SECRET_KEY`: any long random string
   - `DB_HOST`: your MySQL host
   - `DB_PORT`: your MySQL port, usually `3306`
   - `DB_USER`: your MySQL username
   - `DB_PASSWORD`: your MySQL password
   - `DB_NAME`: your MySQL database name
7. Click **Deploy Web Service**.

The included `Procfile` also uses:

```text
web: gunicorn app.main:app --bind 0.0.0.0:${PORT:-8000}
```
