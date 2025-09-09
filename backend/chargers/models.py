from django.db import models
from django.utils import timezone
from accounts.models import User

class Charger(models.Model):
    PLUG_TYPE_CHOICES = [
        ('type2', 'Type2'),
        ('ccs', 'CCS'),
        ('chademo', "CHAdeMO"),
    ]

    STATUS_FREE = 'free'
    STATUS_BOOKED = 'booked'
    STATUS_OCCUPIED = 'occupied'

    STATUS_CHOICES = [
        (STATUS_FREE, 'Free'),
        (STATUS_BOOKED, 'Booked'),
        (STATUS_OCCUPIED, 'Occupied'),
    ]

    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chargers')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    plug_type = models.CharField(max_length=20, choices=PLUG_TYPE_CHOICES, default='type2')
    price_per_kwh = models.DecimalField(max_digits=6, decimal_places=2, default=0.30)
    rating = models.FloatField(default=5.0)
    photo_url = models.CharField(max_length=500, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_FREE)
    status_changed_at = models.DateTimeField(default=timezone.now)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_plug_type_display()})"

    def set_status(self, new_status):
        self.status = new_status
        self.status_changed_at = timezone.now()
        self.save()
