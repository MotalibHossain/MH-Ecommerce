from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Catagory, Product
from shop.utils import CatagoryWiseProduct

# Create your views here.


def Home(request):
    all_catagory = Catagory.objects.all()
    all_product = Product.objects.all()

    # Showing product catagory wise
    context1=CatagoryWiseProduct(all_catagory)

    context = {
        "all_product": all_product,
        "all_catagory": all_catagory,
    }
    # marge two context into single context 
    context.update(context1)
    return render(request, 'shop/index.html',context)


def productDetails(request,slug):
    all_product=Product.objects.all()
    each_product=Product.objects.get(slug=slug)

    context={
        "each_product":each_product,
        "all_product":all_product
    }
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
