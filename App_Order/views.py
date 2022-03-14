from email import message
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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
        userOrder=Order.objects.filter(user=request.user, ordered=False)
        if order_Product_List.orderItem.filter(item=item):
            cardItem[0].quantity+=1
            cardItem[0].save()
            messages.info(request, "Quantity added successfully")
            return HttpResponseRedirect(reverse("shop:productDetails", kwargs={'slug':slug}))
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
    # count how many product add into card through active user 
    number_of_product=Card.objects.filter(user=request.user, purchased=False).count()
    context={
        "all_card_item":all_card_item,
        "number_of_product":number_of_product,
    }
    return render(request, 'Order/shoping-cart.html', context)
