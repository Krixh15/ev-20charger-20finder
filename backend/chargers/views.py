from django.shortcuts import render, get_object_or_404, redirect
from .models import Charger
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def list_chargers(request):
    q = request.GET.get('q', '')
    plug = request.GET.get('plug', '')
    status = request.GET.get('status', '')

    chargers = Charger.objects.filter(is_approved=True)
    if q:
        chargers = chargers.filter(Q(title__icontains=q) | Q(address__icontains=q))
    if plug:
        chargers = chargers.filter(plug_type=plug)
    if status:
        chargers = chargers.filter(status=status)

    return render(request, 'chargers/list.html', {'chargers': chargers})


@login_required
def host_chargers(request):
    # Show chargers owned by the host user
    chargers = Charger.objects.filter(host=request.user)
    return render(request, 'chargers/host_list.html', {'chargers': chargers})


def charger_detail(request, pk):
    charger = get_object_or_404(Charger, pk=pk, is_approved=True)
    return render(request, 'chargers/detail.html', {'charger': charger})
