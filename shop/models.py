from distutils.command.upload import upload
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=30)
    catagory_img=models.ImageField(upload_to='shop/images/catagory/')

    def __str__(self):
        return self.name

        
class Product(models.Model):
    catagory=models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, related_name='Product_catagory')
    name=models.CharField(max_length=80)
    slug=models.SlugField(max_length=80, unique=True)
    description=models.TextField(max_length=500)
    Product_img=models.ImageField(upload_to='shop/images/Product/')
    price=models.DecimalField(max_digits=7, decimal_places=2)
    is_active=models.BooleanField(default=True)
    is_stock=models.BooleanField(default=True)
    published_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name +"-"+ self.slug
    
    class Meta:
        ordering=['-published_date',]

    
