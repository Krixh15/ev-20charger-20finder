from django.contrib import admin
from .models import Charger

@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'plug_type', 'price_per_kwh', 'status', 'is_approved')
    list_filter = ('plug_type', 'status', 'is_approved')
    search_fields = ('title', 'address', 'host__username')
    actions = ['approve_chargers', 'mark_free']

    def approve_chargers(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} chargers approved")
    approve_chargers.short_description = 'Approve selected chargers'

    def mark_free(self, request, queryset):
        for c in queryset:
            c.set_status(Charger.STATUS_FREE)
        self.message_user(request, f"Set {queryset.count()} chargers to FREE")
    mark_free.short_description = 'Set selected chargers to FREE'
