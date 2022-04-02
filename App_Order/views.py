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

# Create your views here.
@login_required
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
            all_card=Card.objects.all()
            all_card_json=django.core.serializers.serialize('python',all_card)
            all_card=django.core.serializers.serialize('json',all_card)

            context={
                "title":"successfully return",
                "all_card_json":all_card_json,
                "all_card":all_card,
            }
            return JsonResponse(context)
        else:
            order_Product_List.orderItem.add(cardItem[0])
            messages.info(request, "Successfully add products.")
            return HttpResponseRedirect(reverse("shop:productDetails", kwargs={'slug':slug}))
    else:
        order=Order(user=request.user)
        order.save()
        order.orderItem.add(cardItem[0])
        messages.info(request, "successfully added")

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
