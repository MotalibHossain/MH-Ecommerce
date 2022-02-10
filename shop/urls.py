from unicodedata import name
from django.urls import path, include
from shop.views import Home, About

app_name="shop"

urlpatterns = [
    path('', Home, name="Home"),
    path('about/', About, name="About"),
]