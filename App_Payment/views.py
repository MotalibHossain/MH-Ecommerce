from django.http import HttpResponse
from django.shortcuts import render

# decorators 
from django.contrib.auth.decorators import login_required

# models 
from App_Order.models import Card, Order
from shop.models import Product
from App_Payment.models import PaymentInfo

# Create your views here.
@login_required
def payment(request):
    if request.user.is_authenticated:
        def get_data_from_post(request, fields):
            form_data=dict()
            for field in fields:
                value=request.POST.get(field)
                form_data[field]=value
            return form_data
        
        if request.method=="POST":
            form_field_data=get_data_from_post(request,["house", "address", "country", "city", "zip"])

            payment_info=PaymentInfo(user=request.user, house=form_field_data['house'],
            address=form_field_data['address'],
            country=form_field_data['country'],
            city=form_field_data['city'],
            zip=form_field_data['zip'])

            print("form field data",form_field_data)
            print("payment_info",payment_info)

            payment_info.save()
        
        payment_info=PaymentInfo.objects.get_or_create(user=request.user)
        order=Order.objects.filter(user=request.user, ordered=False)
        order=order[0]

        context={
            "order":order,
            "payment_info":payment_info
        }

        return render(request, "payment/placeorder.html", context)

