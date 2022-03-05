from email import message
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
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
    cardItem=Card.objects.get_or_create(item=item, user=request.user, purchased=False)
    print("This is card item======", cardItem)
    userOrder=Order.objects.filter(user=request.user, ordered=False)
    print("This is user======", userOrder)
    if userOrder.exists():
        order_Product_List=userOrder[0]
        userOrder=Order.objects.filter(user=request.user, ordered=False)
        print("This is order product======", order_Product_List)
        if order_Product_List.orderItem.filter(item=item):
            cardItem[0].quantity+=1
            cardItem[0].save()
            messages.info(request, "Quantity added successfully")
            # return redirect("shop:Home")
        else:
            order_Product_List.orderItem.add(cardItem[0])
            messages.info(request, "Successfully add products.")
            # return redirect("shop:Home")
    else:
        order=Order(user=request.user)
        order.save()
        order.orderItem.add(cardItem[0])
        messages.info(request, "successfully added")
    
    all_card_item=Card.objects.all()
    context={"all_card_item":all_card_item}
    return render(request, 'Order/shoping-cart.html', context)