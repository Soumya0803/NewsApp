# create_admin.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create admin user if not already created'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                'admin', 'admin@newsapp.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS(
                'Admin user created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))
            
