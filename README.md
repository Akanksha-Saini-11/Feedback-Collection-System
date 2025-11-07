# Feedback Collection System

A lightweight Django application for collecting, managing, and analyzing user feedback. Perfect for gathering customer insights, product reviews, or survey responses with a clean, intuitive interface.

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## Features

✨ **Core Functionality**
- Create, read, update, and delete feedback entries
- Collect user details (name, email, rating 1-5, message)
- Paginated feedback list for easy browsing
- Filter by name and rating using query parameters
- Responsive design with Bootstrap 5

🎨 **User Experience**
- Clean, intuitive interface
- Mobile-friendly layout
- Form validation and error handling
- Confirmation dialogs for destructive actions

## Quick Start

### Prerequisites
- Python 3.9+
- pip and virtualenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Akanksha-Saini-11/Feedback-Collection-System.git
   cd Feedback-Collection-System
   ```

2. **Create and activate a virtual environment**
   
   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
   **macOS/Linux:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   
   Update `feedback_project/settings.py` with your database credentials. The project defaults to MySQL; adjust the `DATABASES` setting as needed:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'feedback_db',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` and start collecting feedback!

## Project Structure

```
Feedback-Collection-System/
├── manage.py                          # Django management script
├── requirements.txt                   # Project dependencies
├── feedback_project/                  # Django project configuration
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # URL routing
│   └── wsgi.py                        # WSGI application
├── feedback_app/                      # Main application
│   ├── migrations/                    # Database migrations
│   ├── templates/feedback_app/        # HTML templates
│   │   ├── base.html                  # Base template with Bootstrap
│   │   ├── feedback_list.html         # List view with pagination
│   │   ├── feedback_detail.html       # Feedback detail view
│   │   ├── feedback_form.html         # Create/edit form
│   │   └── feedback_delete.html       # Confirmation delete
│   ├── static/feedback_app/css/       # Custom stylesheets
│   │   └── styles.css                 # Application styles
│   ├── models.py                      # Database models
│   ├── views.py                       # View controllers
│   ├── forms.py                       # Django forms
│   ├── urls.py                        # App URL patterns
│   └── admin.py                       # Django admin configuration
└── README.md                          # This file
```

## Usage

### Collecting Feedback
1. Click **"Add Feedback"** on the homepage
2. Fill in your details (name, email, message)
3. Select a rating from 1-5 stars
4. Submit the form

### Managing Feedback
- **View all feedback** — Browse the paginated list on the homepage
- **Filter feedback** — Use query parameters: `?name=John&rating=5`
- **Edit feedback** — Click the edit icon to modify an entry
- **Delete feedback** — Click delete and confirm removal

## Configuration

### Database Setup
By default, this project uses MySQL. To use a different database:

**SQLite (development):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**PostgreSQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'feedback_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Environment Variables
For production, store sensitive data in a `.env` file:
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DB_ENGINE=django.db.backends.mysql
DB_NAME=feedback_db
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
```

Install `python-dotenv` and load in `settings.py`:
```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

## Styling

The project uses **Bootstrap 5** for responsive layout and components. Custom styling is centralized in:
- `feedback_app/static/feedback_app/css/styles.css`

Templates inherit from `feedback_app/templates/feedback_app/base.html`, which loads Bootstrap, Google Fonts, and project styles.

## Development

### Running Tests (Coming Soon)
```bash
python manage.py test feedback_app
```

### Code Quality
Install and run linters:
```bash
pip install flake8 pylint
flake8 .
pylint feedback_app/
```

## Production Deployment

Before deploying to production:

1. ✅ **Security Settings**
   ```python
   DEBUG = False
   SECRET_KEY = 'your-secure-random-key'
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']
   ```

2. ✅ **Database**
   - Use environment variables for credentials
   - Set up proper backups
   - Use a production-grade database (PostgreSQL recommended)

3. ✅ **Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. ✅ **HTTPS & Security Headers**
   - Configure SSL/TLS certificates
   - Enable `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, etc.

5. ✅ **Web Server**
   - Use Gunicorn or uWSGI with Nginx reverse proxy
   - Example: `gunicorn feedback_project.wsgi:application`

## Docker Support (Optional)

Create a `Dockerfile` for containerized deployment:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "feedback_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t feedback-app .
docker run -p 8000:8000 feedback-app
```

## Roadmap

- [ ] Unit and integration test suite with GitHub Actions CI/CD
- [ ] User authentication and role-based access control
- [ ] Feedback analytics dashboard (charts, sentiment analysis)
- [ ] Email notifications for new feedback
- [ ] CSV/PDF export functionality
- [ ] Docker Compose setup for local development
- [ ] API endpoints (Django REST Framework)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Support

Found a bug or have a suggestion? Please open an [issue](https://github.com/Akanksha-Saini-11/Feedback-Collection-System/issues) on GitHub.

For questions, feel free to reach out or check the [Django documentation](https://docs.djangoproject.com/).

---

**Built with ❤️ using Django and Bootstrap**
