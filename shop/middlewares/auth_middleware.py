
from django.shortcuts import redirect
from django.urls import reverse_lazy

class authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("auth_middleware")
        if request.user.is_anonymous:
            myUrl=request.META['PATH_INFO']
            return redirect(f'/user/login?myUrl={myUrl}') 

        response = self.get_response(request, *args, **kwargs)
        return response