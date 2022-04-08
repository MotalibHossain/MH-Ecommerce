import django
# model 
from App_Order.models import Card, Order
from shop.models import Product


def CardContext():
    all_card = Card.objects.all()
    all_card_json = django.core.serializers.serialize('python', all_card)
    all_card = django.core.serializers.serialize('json', all_card)
    context = {
        "title": "successfully return",
        "all_card_json":all_card_json,
        "all_card": all_card,
    }
    return context

