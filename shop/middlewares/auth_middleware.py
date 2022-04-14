
from django.shortcuts import redirect
from django.urls import reverse_lazy

class authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print("auth_middleware")
        response = self.get_response(request)
        print("after auth_middleware")
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('App_User:UserLogin'))
        return response


    def process_view(request, view_func, view_args, view_kwargs):
        print("auth_middleware")
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('App_User:UserLogin'))