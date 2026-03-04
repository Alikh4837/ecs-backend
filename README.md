# Django Backend for Software Company Website

## Local Development Setup
1. Create virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and update values
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## API Endpoints
- `POST /api/contact/` - Submit contact form
- `GET /admin/` - Admin panel

## Deployment (Render)
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Add environment variables:
   - `SECRET_KEY`: (generate)
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: your-app.onrender.com,localhost
   - `DATABASE_URL`: (from Render PostgreSQL)
5. Create PostgreSQL database on Render
6. Run migrations via Render Shell: `python manage.py migrate`
7. Create superuser via Render Shell