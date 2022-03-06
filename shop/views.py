from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Catagory, Product
from App_Order.models import Card, Order
from shop.utils import CatagoryWiseProduct

# Create your views here.


def Home(request):
    all_catagory = Catagory.objects.all()
    all_product = Product.objects.all()
    all_card_item=Card.objects.filter(user=request.user, purchased=False)
    order=Order.objects.filter(user=request.user, ordered=False)
    order=order[0]

    # Showing product catagory wise
    context1=CatagoryWiseProduct(all_catagory)

    context = {
        "all_product": all_product,
        "all_catagory": all_catagory,
        "all_card_item":all_card_item,
        "order":order,
    }
    # marge two context into single context 
    context.update(context1)
    return render(request, 'shop/index.html',context)


def productDetails(request,slug):
    all_product=Product.objects.all()
    each_product=Product.objects.get(slug=slug)
    catagory=each_product.catagory
    this_catagory=Product.objects.filter(catagory=catagory)
    all_card_item=Card.objects.filter(user=request.user, purchased=False)

    context={
        "each_product":each_product,
        "all_product":all_product,
        "this_catagory":this_catagory,
        "all_card_item":all_card_item,
    }
    return render(request, 'shop/product-detail.html', context)

def Shop(request):
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
    return render(request, 'shop/product.html', context)


def Features(request):
    return render(request, 'shop/shoping-cart.html')


def Blog(request):
    return render(request, 'shop/blog.html')


def Contact(request):
    return render(request, 'shop/contact.html')


def About(request):
    return render(request, 'shop/about.html')
