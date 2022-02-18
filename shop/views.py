from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Catagory, Product

# Create your views here.


def Home(request):
    all_catagory = Catagory.objects.all()
    all_product = Product.objects.all()

    # Showing product catagory wise
    for cat in all_catagory:
        if str(cat) == 'Man':
            all_man = Product.objects.filter(catagory=cat)
        if str(cat) == 'Women':
            all_women = Product.objects.filter(catagory=cat)
            
    context = {
        "all_product": all_product,
        "all_catagory": all_catagory,
        "all_man": all_man,
        "all_women": all_women,
    }
    return render(request, 'shop/index.html', context)


def productDetails(request,slug):
    myproduct=Product.objects.get(slug=slug)
    context={"product":myproduct}
    return render(request, 'shop/product-detail.html', context)

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
