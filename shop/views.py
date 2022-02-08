from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("This is our Shop app")