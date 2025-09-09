EV Share - Django Backend

This folder contains a starting Django project for the EV Charger Sharing Platform. It is intentionally minimal and uses SQLite for easy local development.

Quick Linux setup (copy/paste):

1. Install Python 3 and venv if you don't have them (Ubuntu/Debian):

   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip

2. Create a virtual environment and activate it:

   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:

   pip install -r requirements.txt

4. Create a .env file by copying from the example and edit keys if needed:

   cp ../.env.example .env

5. Run migrations and create a superuser:

   python manage.py migrate
   python manage.py createsuperuser

6. Start the development server:

   python manage.py runserver 0.0.0.0:8000

Open http://127.0.0.1:8000 in your browser.

Seeding sample data:

This initial skeleton does not yet include seed scripts. Later steps will add a management command to populate sample chargers and users.

Debugging notes:
- If you see "ModuleNotFoundError: dotenv", ensure you installed requirements and activated the virtual environment.
- If templates return 500, check the console logs where runserver is running.
- To run Django checks: python manage.py check

Next steps (I'll implement these in the following tasks):
- Create accounts app with custom user and role management
- Create chargers and bookings apps with models, views, and Razorpay integration
- Add templates, static assets, media uploads, and admin customizations
