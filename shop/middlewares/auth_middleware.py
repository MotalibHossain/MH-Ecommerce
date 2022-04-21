
from django.shortcuts import redirect
from django.urls import reverse_lazy

class authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    # def __call__(self, request):
    #     print("auth_middleware")
    #     response = self.get_response(request)

    #     if not request.user.is_authenticated:
    #         return redirect(reverse_lazy('App_User:UserLogin'))
    #     return response


    def __call__(self, request, *args, **kwargs):
        print("auth_middleware")
        if request.user.is_anonymous:
            myUrl=request.META['PATH_INFO']
            return redirect(f'/user/login?myUrl={myUrl}')
            # return redirect(reverse(f'App_User:UserLogin?myUrl={myUrl}'))     

        response = self.get_response(request, *args, **kwargs)
        return response