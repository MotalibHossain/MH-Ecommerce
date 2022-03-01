from turtle import update
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.
class Card(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="card_User")
    item=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="card_item")
    quantity=models.IntegerField(default=1)
    purchased=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    # total=item.price * quantity

    def __str__(self):
        return f'{self.item.price} X {self.quantity}= {self.item.price * self.quantity}'

    def totalCost(self):
        total=self.item.price * self.quantity
        return total
