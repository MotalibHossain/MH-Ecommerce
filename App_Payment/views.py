from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def payment(request):
    return HttpResponse("we implement our ssl payment method")
