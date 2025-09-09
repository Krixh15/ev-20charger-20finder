EV Charger Sharing Platform - Django (SQLite)

This repository contains a full-stack Django application (development-ready) for an EV Charger Sharing Platform.

Quick start (Linux):

1. Install system dependencies

   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip git

2. Create project folder and clone this repo (if not already)

   git clone <repo_url>
   cd <repo_folder>/backend

3. Create and activate virtualenv

   python3 -m venv .venv
   source .venv/bin/activate

4. Install Python dependencies

   pip install -r requirements.txt

5. Copy environment file and set keys

   cp ../.env.example .env

   # Edit .env and set SECRET_KEY, RAZORPAY keys, GOOGLE_MAPS_API_KEY

6. Create database migrations and migrate

   python manage.py makemigrations
   python manage.py migrate

7. Create a superuser for admin

   python manage.py createsuperuser

8. Seed sample data (creates driver, host, admin, and sample chargers)

   python manage.py seed_data

9. Run the development server

   python manage.py runserver 0.0.0.0:8000

Open http://127.0.0.1:8000 in your browser.

Notes:

- Admin interface: http://127.0.0.1:8000/admin/ (use superuser credentials).
- Razorpay: This project uses Razorpay test keys. Replace RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET in .env with your test keys.
- Google Maps: Replace GOOGLE_MAPS_API_KEY in .env to enable map features (currently placeholder).
- Charger status cycling: Use the management command `python manage.py cycle_chargers` to update charger statuses. Set up a cron job to run it every 5 minutes in production.

Common debugging tips:

- "ModuleNotFoundError": Ensure virtualenv activated and requirements installed.
- "OperationalError: no such table": Did you run migrations? Run `python manage.py migrate`.
- Templates not loading: Ensure TEMPLATES DIRS includes backend/templates and files exist.
- Static files: In dev, Django serves static from STATICFILES_DIRS. Use collectstatic for production.

If you want full PostgreSQL support, or to deploy to production (Gunicorn + Nginx), tell me and I'll add deployment instructions.
