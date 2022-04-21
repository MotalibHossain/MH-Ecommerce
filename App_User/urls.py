from unicodedata import name
from django.urls import path
from App_User.views import UserLogin, UserLogout

app_name='App_User'
urlpatterns = [
    path('user/login', UserLogin.as_view() , name="UserLogin" ),
    path('user/logout', UserLogout , name="UserLogout" ),
    
]
