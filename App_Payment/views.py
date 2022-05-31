from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def payment(request):
    return render(request, "payment/placeorder.html")
