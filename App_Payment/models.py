from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# models 
from App_Order.models import Card, Order
from shop.models import Product

# Create your models here.

class PaymentInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    house=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    zip=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
