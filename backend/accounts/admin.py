from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_approved')
    list_filter = ('role', 'is_approved', 'is_active')
    search_fields = ('username', 'email')
    actions = ['approve_users', 'deactivate_users']

    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Role & Approval', {'fields': ('role', 'is_approved')}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ('Role & Approval', {'fields': ('role', 'is_approved')}),
    )

    def approve_users(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} users approved")
    approve_users.short_description = 'Approve selected users'

    def deactivate_users(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} users deactivated")
    deactivate_users.short_description = 'Deactivate selected users'
