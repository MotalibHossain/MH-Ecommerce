from django.http import HttpResponse
from django.shortcuts import render

# decorators 
from django.contrib.auth.decorators import login_required

# models 
from App_Order.models import Card, Order
from shop.models import Product

# Create your views here.
@login_required
def payment(request):
    if request.user.is_authenticated:
        order=Order.objects.filter(user=request.user, ordered=False)
        order=order[0]
        context={
            "order":order,
        }

        return render(request, "payment/placeorder.html", context)

    else:
        order=Order.objects.filter(user=request.user, ordered=False)
        order=order[0]
        context={
            "order":order,
        }

        return render(request, "payment/placeorder.html", context)

