
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from App_Order.views import card, Card_View

app_name="App_Order"

urlpatterns = [
    path('card/<int:id>', card, name="card"),
    path('Card_View/', Card_View, name="Card_View"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
