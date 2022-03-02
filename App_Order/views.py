from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# decorators 
from django.contrib.auth.decorators import login_required
 
# model 
from App_Order.models import Card
from shop.models import Product

# Create your views here.
@login_required
def card(request,id):
    item=get_object_or_404(Product, id=id)
    Card.objects.get_or_create(item=item, user=request.user, purchased=False)
    all_card_item=Card.objects.all()
    print(all_card_item)
    context={"all_card_item":all_card_item}
    return render(request, 'Order/shoping-cart.html',context)