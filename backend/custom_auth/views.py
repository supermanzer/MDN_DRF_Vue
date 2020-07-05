from django.http.response import JsonResponse
import django
# Create your views here.


def get_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})
