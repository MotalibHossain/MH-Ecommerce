import imp
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('shop:Home'))
        else:
            return redirect(reverse_lazy('App_User:UserLogin'))

    return render(request, 'User/login.html')


def UserLogout(request):
    logout(request)
    return redirect(reverse_lazy('shop:Home'))
