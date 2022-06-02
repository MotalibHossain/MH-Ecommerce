
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from App_Order.views import card, Card_View

# middlewares 
from django.utils.decorators import method_decorator
from .middlewares.auth_middleware import authmiddleware

app_name="App_Order"

urlpatterns = [
    path('card/<int:id>', authmiddleware(card), name="card"),
    path('Card_View/', Card_View, name="Card_View"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
