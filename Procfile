release: python manage.py migrate && chmod u+x create_superuser.sh && ./create_superuser.sh
web: python manage.py migrate && gunicorn telusko.wsgi
