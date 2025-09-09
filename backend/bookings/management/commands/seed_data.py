from django.core.management.base import BaseCommand
from accounts.models import User
from chargers.models import Charger
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed sample users and chargers for development'

    def handle(self, *args, **options):
        # Create users
        if not User.objects.filter(username='driver@example.com').exists():
            driver = User.objects.create_user(username='driver@example.com', email='driver@example.com', password='password')
            driver.first_name = 'Driver'
            driver.role = User.ROLE_DRIVER
            driver.save()
            self.stdout.write('Created driver user')
        if not User.objects.filter(username='host@example.com').exists():
            host = User.objects.create_user(username='host@example.com', email='host@example.com', password='password')
            host.first_name = 'Host'
            host.role = User.ROLE_HOST
            host.is_approved = True
            host.save()
            self.stdout.write('Created host user')
        if not User.objects.filter(username='admin@example.com').exists():
            admin = User.objects.create_user(username='admin@example.com', email='admin@example.com', password='password')
            admin.first_name = 'Admin'
            admin.role = User.ROLE_ADMIN
            admin.is_staff = True
            admin.is_superuser = True
            admin.is_approved = True
            admin.save()
            self.stdout.write('Created admin user')

        # Create sample chargers
        host = User.objects.filter(role=User.ROLE_HOST).first()
        if host and not Charger.objects.exists():
            Charger.objects.create(host=host, title='Sample Home Charger', address='123 Main St', plug_type='type2', price_per_kwh=0.30, rating=4.8, is_approved=True)
            Charger.objects.create(host=host, title='Mall Charger', address='Mall Rd', plug_type='ccs', price_per_kwh=0.25, rating=4.5, is_approved=True)
            self.stdout.write('Created sample chargers')

        self.stdout.write(self.style.SUCCESS('Seeding completed'))
