from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with email and password'

    def handle(self, *args, **options):
        email = input("Enter email: ").lower()
        password = input("Enter Password: ")
        User.objects.create_superuser(email=email, username=email, password=password)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))