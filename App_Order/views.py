from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def card(request):
    return HttpResponse("card app")