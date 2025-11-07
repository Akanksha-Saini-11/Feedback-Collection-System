# Feedback Collection System

A small Django app to collect, view, and manage user feedback (name, email, rating, message).

This repository contains a clean, minimal feedback system implemented with Django. The UI uses Bootstrap and custom styles located under the app's static folder.

## Quick start (development)

1. Create a virtual environment and activate it (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Configure the database:

- The project expects a database configured in `feedback_project/settings.py`. By default this project was developed with MySQL. Update the `DATABASES` settings to match your environment.

4. Apply migrations and run the server:

```powershell
python manage.py migrate
python manage.py runserver
```

5. Open your browser at http://127.0.0.1:8000/


## Project structure (important files)

- `manage.py` — Django management entrypoint.
- `feedback_project/` — Django project settings and WSGI/URLs.
- `feedback_app/` — Main app containing models, views, forms, templates and static files.
  - `templates/feedback_app/` — Django templates for list, detail, form, and delete views.
  - `static/feedback_app/css/styles.css` — Central stylesheet used across templates.
  - `forms.py`, `models.py`, `views.py` — app logic.

## Styling and templates

- The project uses Bootstrap 5 for layout and components. Custom styling is kept in `feedback_app/static/feedback_app/css/styles.css`.
- Templates extend `feedback_app/base.html` which loads Bootstrap, Google Fonts and the project stylesheet.

## Features

- Add feedback (name, email, rating 1-5, message).
- Edit and delete feedback.
- Paginated list of feedbacks.
- Filtering by name and rating (via query string parameters).

## Testing & linting

This repository does not include an automated test suite by default. For a production-ready setup consider adding unit tests (Django TestCase), linters (flake8, pylint), and a CI pipeline.

## Notes & next steps

- Update `settings.py` with secure settings for production (SECRET_KEY, DEBUG, ALLOWED_HOSTS).
- Add a `.env` or secrets manager for DB credentials.
- Consider extracting common UI bits (header/footer) into template includes if expanding the project.

If you'd like, I can:
- Add a CONTRIBUTING.md and CODE_OF_CONDUCT.md
- Add a short developer checklist with typical local setup steps
- Create a small test suite (happy-path for views) and a GitHub Actions workflow to run it

---

If you'd like any changes to the README (more/less detail, different setup commands, add Docker instructions), tell me which parts to expand or change.