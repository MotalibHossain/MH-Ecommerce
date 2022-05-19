from urllib import request
import django
# model 
from App_Order.models import Card, Order
from shop.models import Product

def CardContext(request):
    all_card = Card.objects.filter(user=request.user, purchased=False)
    # Convert python object to python json data 
    all_card_json = django.core.serializers.serialize('python', all_card)
    # convert python json formate to javaScript json formate 
    all_card = django.core.serializers.serialize('json', all_card)
    context = {
        "title": "successfully return",
        "all_card_json":all_card_json,
        "all_card": all_card,
    }
    return context
