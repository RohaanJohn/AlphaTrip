# myapp/management/commands/createsuperuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('Rohaan', type=str)
        parser.add_argument('rohaanjohn0@gmai.com', type=str)
        parser.add_argument('1234', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(f'Successfully created superuser {username}')
