release: python manage.py migrate && python manage.py createsuperuser --username superuser --email superuser@example.com --password password --noinput --database default
web: python manage.py migrate && gunicorn telusko.wsgi
