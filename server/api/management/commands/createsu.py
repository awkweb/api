from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a super user for when TTY mode is unavailable'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs='?')
        parser.add_argument('password', nargs='?')

    def handle(self, *args, **options):
        email = options['email']
        if not get_user_model().objects.filter(email=email).exists():
            password = options['password']
            get_user_model().objects.create_superuser(email, password)
