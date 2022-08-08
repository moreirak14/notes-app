from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def get(request):
    return JsonResponse("API", safe=False)
