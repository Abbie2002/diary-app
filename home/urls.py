from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
]
