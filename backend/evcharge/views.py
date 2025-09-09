from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User

# Home view
def home(request):
    return render(request, 'index.html')

# Login view: handles GET (show form) and POST (authenticate)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Using email as username
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active and user.is_approved:
            login(request, user)
            # Redirect based on role
            if user.role == User.ROLE_HOST:
                return redirect('host_dashboard')
            if user.role == User.ROLE_ADMIN:
                return redirect('admin_dashboard')
            return redirect('driver_dashboard')
        messages.error(request, 'Invalid credentials or account not approved')
    return render(request, 'login.html')

# Signup view: create user and log them in
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', User.ROLE_DRIVER)
        # Username must be unique; we'll use the email as username
        if User.objects.filter(username=email).exists():
            messages.error(request, 'A user with that email already exists')
            return render(request, 'signup.html')
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.role = role
        # Hosts require admin approval by default
        user.is_approved = False if role == User.ROLE_HOST else True
        if role == User.ROLE_ADMIN:
            user.is_staff = True
            user.is_superuser = True
            user.is_approved = True
        user.save()
        # Log the user in
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            if user.role == User.ROLE_HOST:
                return redirect('host_dashboard')
            if user.role == User.ROLE_ADMIN:
                return redirect('admin_dashboard')
            return redirect('driver_dashboard')
    return render(request, 'signup.html')

# Simple dashboards and pages
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
