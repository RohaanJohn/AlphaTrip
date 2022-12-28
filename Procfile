release: python manage.py migrate && chmod +x __init__.py && ./management/__init__.py
web: python manage.py migrate && gunicorn telusko.wsgi
