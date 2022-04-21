
from django.shortcuts import redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.urls import resolve
from decouple import config


class authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request, *args, **kwargs):
        # This code for return url when user is not login but wants to add product add to cart.
        # then redirect into login page and get back privious page when successfully login.
        if request.user.is_anonymous:
            # Get current current full url 
            myUrl=request.META["HTTP_REFERER"]
            # Import domain part from env using decouple package  
            p=config('DOMAIN_URL')
            # Remove domain part from full url 
            myUrl=myUrl.replace(p, "")
            return redirect(f'/user/login?myUrl={myUrl}')    

        response = self.get_response(request, *args, **kwargs)
        return response