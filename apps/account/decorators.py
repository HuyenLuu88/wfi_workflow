from django.conf import settings
from django.contrib import messages
from django.db.models import Sum
from functools import wraps


# from axes.attempts import (
#     get_user_attempts,
# )

import requests


# def check_recaptcha_login(view_func, credentials: dict = None):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#
#         attempts_list = get_user_attempts(request, credentials)
#
#         attempt_count = max(
#             (
#                     attempts.aggregate(Sum("failures_since_start"))[
#                         "failures_since_start__sum"
#                     ]
#                     or 0
#             )
#             for attempts in attempts_list
#         )
#         print(attempt_count)
#
#         attempt_count = attempt_count
#
#
#
#         request.recaptcha_is_valid = None
#         if request.method == 'POST':
#             recaptcha_response = request.POST.get('g-recaptcha-response')
#             data = {
#                 'secret': settings.RECAPTCHA_PRIVATE_KEY,
#                 'response': recaptcha_response
#             }
#             r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#             result = r.json()
#             if result['success']:
#                 request.recaptcha_is_valid = True
#             else:
#                 request.recaptcha_is_valid = False
#
#                 if attempt_count > 2:
#                     messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#
#
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view


def check_recaptcha_form(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            #r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            #result = r.json()
            #if result['success']:
            request.recaptcha_is_valid = True
            #else:
            #    request.recaptcha_is_valid = False

            #    messages.error(request, 'Invalid reCAPTCHA. Please try again.')


        return view_func(request, *args, **kwargs)
    return _wrapped_view