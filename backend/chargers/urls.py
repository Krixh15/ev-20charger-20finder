from django.urls import path
from . import views

app_name = 'chargers'

urlpatterns = [
    path('', views.list_chargers, name='list'),
    path('host/', views.host_chargers, name='host_list'),
    path('<int:pk>/', views.charger_detail, name='detail'),
]
