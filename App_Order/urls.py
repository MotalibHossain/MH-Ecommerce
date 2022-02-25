
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from App_Order.views import card

app_name="App_Order"

urlpatterns = [
    path('card/', card, name="card"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
