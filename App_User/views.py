from modulefinder import IMPORT_NAME
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def UserLogin(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         myUrl=myUrl
#         print("my url is here",myUrl)
#         user=authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             myUrl=request.GET.get('myUrl')
#             print("my url is here",myUrl)

#             # middleware redirection code 

#             # if myUrl:
#             #     print("redirect user", myUrl)
#             #     return HttpResponseRedirect(myUrl)
#             # else:
#             #     print("home page",myUrl)
#             #     # myUrl=None
#             #     return redirect(reverse_lazy('shop:Home'))
#         else:
#             return redirect(reverse_lazy('App_User:UserLogin'))

#     return render(request, 'User/login.html')



class UserLogin(View):
    myUrl=None

    def get(self,request):
        UserLogin.myUrl=request.GET.get('myUrl')
        print("my url is here",UserLogin.myUrl)
        return render(request, 'User/login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # middleware redirection code 

            if UserLogin.myUrl:
                print("redirect user", UserLogin.myUrl)
                return HttpResponseRedirect(UserLogin.myUrl)
            else:
                print("home page",UserLogin.myUrl)
                UserLogin.myUrl=None
            return redirect(reverse_lazy('shop:Home'))
        else:
            return redirect(reverse_lazy('App_User:UserLogin'))


def UserLogout(request):
    logout(request)
    return redirect(reverse_lazy('shop:Home'))
