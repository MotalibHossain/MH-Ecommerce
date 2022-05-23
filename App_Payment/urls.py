from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from App_Payment.views import payment


app_name="App_Payment"

urlpatterns = [
    path('payment/', payment, name="payment"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)