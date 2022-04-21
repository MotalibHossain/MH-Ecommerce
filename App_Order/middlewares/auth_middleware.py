
from django.shortcuts import redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.urls import resolve
from decouple import config


class authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request, *args, **kwargs):
        print("auth_middleware")
        if request.user.is_anonymous:
            # myUrl=request.META['PATH_INFO']
            # myUrl="/productDetails/Solid-Mens-Cotton/"
            myUrl=request.META["HTTP_REFERER"]
            p=config('DOMAIN_URL')
            myUrl=myUrl.replace(p, "")
            return redirect(f'/user/login?myUrl={myUrl}')
            # return redirect(reverse(f'App_User:UserLogin?return_url={return_url}'))     

        response = self.get_response(request, *args, **kwargs)
        return response
    
    # def process_view(request, view_func, view_args, view_kwargs):
    #     print("auth_middleware")
    #     if not request.user.is_authenticated:
    #         return redirect(reverse_lazy('App_User:UserLogin'))