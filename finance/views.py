# finance/views.py
from django.http import JsonResponse

def finance_home(request):
    return JsonResponse({"message": "Finance home endpoint"})
