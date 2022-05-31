from django.http import HttpResponse
from django.shortcuts import render




# Create your views here.

def payment(request):
    order=Order.objects.filter(user=request.user, ordered=False)
    order=order[0]
    number_of_product=Order.objects.filter(user=request.user, ordered=False).count() 
    context={
        "all_card_item":all_card_item,
        "order":order,
        "number_of_product":number_of_product,
    }

    return render(request, "payment/placeorder.html")
