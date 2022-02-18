from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from shop.views import (
    Home,
    Shop,
    Features,
    Blog,
    Contact, 
    About,
    productDetails,
)

app_name="shop"

urlpatterns = [
    path('', Home, name="Home"),
    path('shop/', Shop, name="Shop"),
    path('features/', Features, name="Features"),
    path('blog/', Blog, name="Blog"),
    path('contact/', Contact, name="Contact"),
    path('about/', About, name="About"),
    path('productDetails/<str:slug>', productDetails, name="productDetails"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
