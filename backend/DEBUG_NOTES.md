Debugging Notes for Beginners

1. Virtual environment & dependencies

- Activate the venv: `source .venv/bin/activate`
- Install packages: `pip install -r requirements.txt`
- If a module is missing, pip install it and re-run.

2. Database migration issues

- If you see errors like "no such table", run:
  python manage.py makemigrations
  python manage.py migrate
- If migrations fail, read the full traceback and ensure models.py syntax is valid.

3. Static files & templates

- Templates path: backend/templates. If a template is not found, check the file name and TEMPLATES DIRS in settings.
- Static path: backend/static. In development, runserver serves static automatically.

4. Razorpay payments

- Use test keys in .env. Razorpay expects INR and amounts in paise (multiply by 100). The demo code skips signature verification — implement it for production.

5. Common commands

- Run server: python manage.py runserver
- Create superuser: python manage.py createsuperuser
- Seed data: python manage.py seed_data
- Cycle chargers status: python manage.py cycle_chargers

6. Logs

- The development server prints logs to terminal. Check exception tracebacks to locate failing files/lines.

7. Troubleshooting

- "AttributeError: module 'X' has no attribute Y" usually means circular imports. Check imports between apps.
- If migrations are inconsistent, try `python manage.py migrate --fake appname zero` then `makemigrations` and `migrate` carefully.
