from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'shop/index.html')

    
def Shop(request):
    return render(request, 'shop/product.html')

    
def Features(request):
    return render(request, 'shop/shoping-cart.html')


def Blog(request):
    return render(request, 'shop/blog.html')


def Contact(request):
    return render(request, 'shop/contact.html')


def About(request):
    return render(request, 'shop/about.html')
