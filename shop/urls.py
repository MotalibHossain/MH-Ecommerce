from unicodedata import name
from django.urls import path, include
from shop.views import Home

urlpatterns = [
    path(' ', Home, name="Home"),
]