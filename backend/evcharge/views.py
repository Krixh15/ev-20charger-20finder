from django.shortcuts import render
from django.http import HttpResponse

# Simple views that render templates. These are intentionally minimal while we
# build out the full feature set step-by-step.

def home(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


def driver_dashboard(request):
    return render(request, 'driver_dashboard.html')


def host_dashboard(request):
    return render(request, 'host_dashboard.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def booking_page(request):
    return render(request, 'booking.html')


def payments_page(request):
    return render(request, 'payments.html')


def reviews_page(request):
    return render(request, 'reviews.html')


def contact_page(request):
    return render(request, 'contact.html')


def terms_page(request):
    return render(request, 'terms.html')


def privacy_page(request):
    return render(request, 'privacy.html')


# Custom error handlers

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
