from pyexpat import model
from turtle import update
from urllib import request
from venv import create
from django.shortcuts import redirect
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
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
    def get_absolute_url(self):
        return reverse_lazy('App_Order:card', args=[self.id])
        # return reverse_lazy('App_Order:card', args=[self.slug])

class Order(models.Model):
    orderItem=models.ManyToManyField(Card)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    orderId=models.CharField(max_length=80)
    paymentId=models.CharField(max_length=80)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    def orderTotal(self):
        total=0
        for orderitem in self.orderItem.all():
            print(orderitem)
            total+=orderitem.totalCost()
            print(total)
            return total
            
    def __str__(self):
        return f'{self.user} ---> {self.orderId}'