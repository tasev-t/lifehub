from django.http import JsonResponse

def pets_home(request):
    return JsonResponse({"message": "Pets home endpoint"})
