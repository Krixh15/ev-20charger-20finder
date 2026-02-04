import razorpay
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from accounts.models import User
from chargers.models import Charger
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse

def get_razorpay_client():
    if not settings.RAZORPAY_KEY_ID or not settings.RAZORPAY_KEY_SECRET:
        return None
    return razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def list_bookings(request):
    if request.user.role == User.ROLE_HOST:
        bookings = Booking.objects.filter(charger__host=request.user)
        heading = "Host Bookings"
    else:
        bookings = Booking.objects.filter(driver=request.user)
        heading = "Your Bookings"

    return render(
        request,
        "bookings/list.html",
        {
            "bookings": bookings.select_related("charger", "driver"),
            "heading": heading,
        },
    )

@login_required
def create_booking(request):
    # Simple booking creation from POST data
    if request.method == 'POST':
        charger_id = request.POST.get('charger')
        start = request.POST.get('start')
        end = request.POST.get('end')
        amount = request.POST.get('amount')
        charger = get_object_or_404(Charger, pk=charger_id)
        booking = Booking.objects.create(
            driver=request.user,
            charger=charger,
            start=start,
            end=end,
            amount=amount,
            status=Booking.STATUS_CREATED,
        )
        # Mark charger as booked
        charger.set_status(Charger.STATUS_BOOKED)
        return redirect('bookings:payment', booking.id)
    # If GET, show a basic form
    chargers = Charger.objects.filter(is_approved=True)
    return render(request, 'bookings/create.html', {'chargers': chargers})

@login_required
def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, driver=request.user)
    razorpay_client = get_razorpay_client()
    if not razorpay_client:
        if request.method == 'POST':
            booking.status = Booking.STATUS_PAID
            booking.save()
            charger = booking.charger
            charger.set_status(Charger.STATUS_OCCUPIED)
            return redirect('bookings:thankyou', booking.pk)
        return render(request, 'bookings/payment.html', {
            'booking': booking,
            'dummy_payment': True,
        })

    # Create razorpay order
    amount_paise = int(float(booking.amount) * 100)
    razorpay_order = razorpay_client.order.create(dict(amount=amount_paise, currency='INR', payment_capture='1'))
    booking.razorpay_order_id = razorpay_order['id']
    booking.save()
    context = {
        'booking': booking,
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'order_id': razorpay_order['id'],
        'amount': amount_paise,
        'dummy_payment': False,
    }
    return render(request, 'bookings/payment.html', context)

@csrf_exempt
def payment_callback(request):
    # Razorpay sends payment info to client; here we accept a POST from client to confirm.
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        booking = get_object_or_404(Booking, pk=booking_id)
        # NOTE: In production, verify signature using razorpay utility. For test/demo we accept.
        booking.razorpay_payment_id = payment_id
        booking.status = Booking.STATUS_PAID
        booking.save()
        # Update charger status to occupied
        charger = booking.charger
        charger.set_status(Charger.STATUS_OCCUPIED)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'invalid'}, status=400)

@login_required
def thankyou(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, driver=request.user)
    return render(request, 'bookings/thankyou.html', {'booking': booking})
