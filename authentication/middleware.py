import re

from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLs = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URL'):
	EXEMPT_URLs += [re.compile(url) for url in settings.LOGIN_EXEMPT_URL]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kargs):
    	#assert hasattr(request, 'user')
    	path = request.path_info.lstrip('/')
    	print(path)

    	if not request.user.is_authenticated:
    		if not any(url.match(path) for url in EXEMPT_URLs):
    			return redirect(settings.LOGIN_URL)
