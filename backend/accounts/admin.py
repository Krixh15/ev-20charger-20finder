from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_approved')
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Role & Approval', {'fields': ('role', 'is_approved')}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ('Role & Approval', {'fields': ('role', 'is_approved')}),
    )
