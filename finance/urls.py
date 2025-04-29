# finance/urls.py
from django.urls import path
from .views import finance_home

urlpatterns = [
    path('', finance_home, name='finance-home'),
]
