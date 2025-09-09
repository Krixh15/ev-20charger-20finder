from django.core.management.base import BaseCommand
from chargers.models import Charger
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Cycle charger statuses: BOOKED -> OCCUPIED -> FREE based on time thresholds'

    def handle(self, *args, **options):
        now = timezone.now()
        # If a charger is BOOKED for more than 30 minutes, mark OCCUPIED
        booked_threshold = now - timedelta(minutes=30)
        booked = Charger.objects.filter(status=Charger.STATUS_BOOKED, status_changed_at__lt=booked_threshold)
        for c in booked:
            self.stdout.write(f"Setting {c} to OCCUPIED")
            c.set_status(Charger.STATUS_OCCUPIED)

        # If a charger is OCCUPIED for more than 2 hours, mark FREE
        occupied_threshold = now - timedelta(hours=2)
        occupied = Charger.objects.filter(status=Charger.STATUS_OCCUPIED, status_changed_at__lt=occupied_threshold)
        for c in occupied:
            self.stdout.write(f"Setting {c} to FREE")
            c.set_status(Charger.STATUS_FREE)

        self.stdout.write(self.style.SUCCESS('Charger status cycle completed'))
