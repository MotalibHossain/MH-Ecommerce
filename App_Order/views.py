from email import message
import mimetypes
from multiprocessing import context
from turtle import title
import django
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
# decorators 
from django.contrib.auth.decorators import login_required
 
# model 
from App_Order.models import Card, Order
from shop.models import Product

# utils functions 
from App_Order.utils import CardContext

# # middlewares 
# from django.utils.decorators import method_decorator
# from .middlewares.auth_middleware import authmiddleware


# Create your views here.
# @login_required
# @authmiddleware
def card(request,id):
    item=get_object_or_404(Product, id=id)
    slug=item.slug
    cardItem=Card.objects.get_or_create(item=item, user=request.user, purchased=False)
    userOrder=Order.objects.filter(user=request.user, ordered=False)

    if userOrder.exists():
        order_Product_List=userOrder[0]
        # userOrder=Order.objects.filter(user=request.user, ordered=False)
        if order_Product_List.orderItem.filter(item=item).exists():
            cardItem[0].quantity+=1
            cardItem[0].save()

            context=CardContext()
            return JsonResponse(context)
        else:
            order_Product_List.orderItem.add(cardItem[0])

            context=CardContext()
            return JsonResponse(context)
    else:
        order=Order(user=request.user)
        order.save()
        order.orderItem.add(cardItem[0])

        context=CardContext()
        return JsonResponse(context)


@login_required
def Card_View(request):
    all_card_item=Card.objects.filter(user=request.user, purchased=False)
    order=Order.objects.filter(user=request.user, ordered=False)
    order=order[0]
    number_of_product=Order.objects.filter(user=request.user, ordered=False).count() 
    context={
        "all_card_item":all_card_item,
        "order":order,
        "number_of_product":number_of_product,
    }
    return render(request, 'Order/shoping-cart.html', context)
