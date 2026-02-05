from django.core.management.base import BaseCommand
from accounts.models import User
from chargers.models import Charger
class Command(BaseCommand):
    help = 'Seed sample users and chargers for development'

    def handle(self, *args, **options):
        # Create or refresh users so credentials stay predictable in development
        driver, driver_created = User.objects.get_or_create(
            username='driver@example.com',
            defaults={'email': 'driver@example.com'},
        )
        driver.first_name = 'Driver'
        driver.role = User.ROLE_DRIVER
        driver.is_approved = True
        driver.is_active = True
        driver.set_password('StrongPass123!')
        driver.save()
        self.stdout.write(
            ('Created' if driver_created else 'Updated')
            + ' driver user (email: driver@example.com, password: StrongPass123!)'
        )

        host, host_created = User.objects.get_or_create(
            username='host@example.com',
            defaults={'email': 'host@example.com'},
        )
        host.first_name = 'Host'
        host.role = User.ROLE_HOST
        host.is_approved = True
        host.is_active = True
        host.set_password('StrongPass123!')
        host.save()
        self.stdout.write(
            ('Created' if host_created else 'Updated')
            + ' host user (email: host@example.com, password: StrongPass123!)'
        )

        admin, admin_created = User.objects.get_or_create(
            username='admin@example.com',
            defaults={'email': 'admin@example.com'},
        )
        admin.first_name = 'Admin'
        admin.role = User.ROLE_ADMIN
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_approved = True
        admin.is_active = True
        admin.set_password('StrongPass123!')
        admin.save()
        self.stdout.write(
            ('Created' if admin_created else 'Updated')
            + ' admin user (email: admin@example.com, password: StrongPass123!)'
        )

        # Create sample chargers
        host = User.objects.filter(role=User.ROLE_HOST).first()
        if host and not Charger.objects.exists():
            Charger.objects.create(host=host, title='Sample Home Charger', address='123 Main St', plug_type='type2', price_per_kwh=0.30, rating=4.8, is_approved=True)
            Charger.objects.create(host=host, title='Mall Charger', address='Mall Rd', plug_type='ccs', price_per_kwh=0.25, rating=4.5, is_approved=True)
            self.stdout.write('Created sample chargers')

        self.stdout.write(self.style.SUCCESS('Seeding completed'))
