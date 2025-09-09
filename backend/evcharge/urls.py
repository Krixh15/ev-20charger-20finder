from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = 'evcharge.views.custom_404'
handler500 = 'evcharge.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('driver/dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('host/dashboard/', views.host_dashboard, name='host_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('booking/', views.booking_page, name='booking'),
    path('chargers/', include('chargers.urls')),
    path('bookings/', include('bookings.urls')),
    path('payments/', views.payments_page, name='payments'),
    path('reviews/', views.reviews_page, name='reviews'),
    path('contact/', views.contact_page, name='contact'),
    path('terms/', views.terms_page, name='terms'),
    path('privacy/', views.privacy_page, name='privacy'),
]
