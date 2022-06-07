from genericpath import exists
from turtle import ht
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from App_Payment.utils import get_data_from_post

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
        all_card_item=Card.objects.filter(user=request.user, purchased=False)
        payment_info=PaymentInfo.objects.filter(user=request.user)

        if request.method=="POST":
            form_field_data=get_data_from_post(request,["house", "address", "country", "city", "zip"])

            Billing_info=PaymentInfo(user=request.user, house=form_field_data['house'],
            address=form_field_data['address'],
            country=form_field_data['country'],
            city=form_field_data['city'],
            zip=form_field_data['zip'])

            if payment_info.exists():
                payment_info.update(user=request.user, house=form_field_data['house'],
                                    address=form_field_data['address'],
                                    country=form_field_data['country'],
                                    city=form_field_data['city'],
                                    zip=form_field_data['zip'])
            else:
                Billing_info.save()
        
        order=Order.objects.filter(user=request.user, ordered=False)

        context={
            "order":order,
            "payment_info":payment_info,
            "all_card_item":all_card_item,
        }

        return render(request, "payment/placeorder.html", context)

@login_required
def BillPay(request):
    all_card_item=Card.objects.filter(user=request.user, purchased=False)
    payment_info=PaymentInfo.objects.get_or_create(user=request.user)

    if payment_info[0].is_all_filled():
        return HttpResponse("pay bill")
    else:
        return redirect (reverse_lazy('App_Payment:payment'))

