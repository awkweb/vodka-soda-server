from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a super user for when TTY mode is unavailable'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?')
        parser.add_argument('email', nargs='?')
        parser.add_argument('password', nargs='?')

    def handle(self, *args, **options):
        username = options['username']
        if not get_user_model().objects.filter(username=username).exists():
            email = options['email']
            password = options['password']
            get_user_model().objects.create_superuser(username, email, password)
