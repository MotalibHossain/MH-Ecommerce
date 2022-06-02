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

        def get_data_from_post(request, fields):
            form_data=dict()
            for field in fields:
                value=request.Post.get("field")
                form_data[field]=value
            return form_data
        
        if request.method=="POST":
            form_field_data=get_data_from_post(request,["house", "address", "country", "city", "zip"])





        context={
            "order":order,
        }

        return render(request, "payment/placeorder.html", context)

