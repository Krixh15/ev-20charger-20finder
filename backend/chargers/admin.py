from django.contrib import admin
from .models import Charger

@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'plug_type', 'price_per_kwh', 'status', 'is_approved')
    list_filter = ('plug_type', 'status', 'is_approved')
    search_fields = ('title', 'address', 'host__username')
