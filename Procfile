release: python manage.py migrate && python -m django_createsuperuser "rohaan" "1234"
web: python manage.py migrate && gunicorn telusko.wsgi
