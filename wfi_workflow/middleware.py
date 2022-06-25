from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from wfi_workflow.settings import base
from django_otp import user_has_device
from django_otp.decorators import otp_required
from django_otp.middleware import is_verified

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings by setting a tuple of routes to ignore
    """

    def process_request(self, request):
        assert hasattr(request, 'user'), """
        The Login Required middleware needs to be after AuthenticationMiddleware.
        Also make sure to include the template context_processor:
        'django.contrib.account.context_processors.account'."""


        if not request.user.is_verified() and not request.path.startswith('/admin/') and not request.path.startswith('/account/') and not request.path.startswith('/chaining/') and not request.path.startswith('/ajax/load-offices/'):

            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in base.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(base.LOGIN_URL))

