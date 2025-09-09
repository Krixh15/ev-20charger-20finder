from django.db import models
from django.utils import timezone
from accounts.models import User
from chargers.models import Charger

class Booking(models.Model):
    STATUS_CREATED = 'created'
    STATUS_PAID = 'paid'
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'Created'),
        (STATUS_PAID, 'Paid'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE, related_name='bookings')
    start = models.DateTimeField()
    end = models.DateTimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CREATED)

    created_at = models.DateTimeField(auto_now_add=True)

    # Payment fields
    razorpay_order_id = models.CharField(max_length=200, blank=True)
    razorpay_payment_id = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Booking {self.pk} by {self.driver} for {self.charger}"
