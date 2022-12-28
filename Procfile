release: python manage.py migrate && python manage.py createsuperuser --username superuser --password password --noinput
web: python manage.py migrate && gunicorn telusko.wsgi
