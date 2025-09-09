from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/', views.create_booking, name='create'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment'),
    path('payment-callback/', views.payment_callback, name='payment_callback'),
    path('thankyou/<int:booking_id>/', views.thankyou, name='thankyou'),
]
