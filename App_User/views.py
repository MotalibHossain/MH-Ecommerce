from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def UserLogin(request):
    # myUrl=None
    myUrl=request.GET.get('myUrl')
    print("11111111111111",myUrl)
    

    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        myUrl=myUrl
        print("my url is here",myUrl)
        user=authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # myUrl=request.GET.get('myUrl')
            # print("my url is here",myUrl)

            if myUrl:
                print("redirect user", myUrl)
                return HttpResponseRedirect(myUrl)
            else:
                print("home page",myUrl)
                # myUrl=None
                return redirect(reverse_lazy('shop:Home'))
        else:
            return redirect(reverse_lazy('App_User:UserLogin'))

    return render(request, 'User/login.html')


def UserLogout(request):
    logout(request)
    return redirect(reverse_lazy('shop:Home'))
