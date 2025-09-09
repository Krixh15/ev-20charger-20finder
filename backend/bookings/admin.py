from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'charger', 'start', 'end', 'amount', 'status')
    list_filter = ('status',)
    search_fields = ('driver__username', 'charger__title')
