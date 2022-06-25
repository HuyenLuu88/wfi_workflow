# from django.db.models import Sum
# from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import View

from .forms import RegisterForm

from .models import User

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
# from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .utils import generate_user_token, generate_admin_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.conf import settings
import threading
# import datetime
from .decorators import check_recaptcha_form
# from axes.decorators import axes_dispatch
from django_otp.plugins.otp_totp.models import TOTPDevice
from apps.account.models import User, Office, Country
from apps.account.forms import RegisterForm, PersonalInfoForm, SecurityForm #, twofaForm



# from axes.attempts import (
#     clean_expired_user_attempts,
#     get_user_attempts,
#     reset_user_attempts,
# )
from django.utils.decorators import method_decorator


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_email(user, request, email_subject, email_body, uid, token, to_email):
    current_site = get_current_site(request)
    email_subject = email_subject
    email_body = render_to_string(email_body, {
        'user': user,
        'domain': current_site,
        'site_name': 'WFI Workflow System',
        'uid': uid,
        'token': token,
        'protocol': settings.DOMAIN_PROTOCOL,
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=to_email
                         )

    EmailThread(email).start()




def account(request):

    if request.user.is_authenticated:

        # from django_countries import countries
        #
        # with open('countries.txt', 'w') as f:
        #     x = 0
        #     for code, name in list(countries):
        #         x += 1
        #         print(str(x) + '\t' + name + '\t' + code + '\n')
        #         #f.write("%s\n" % code)
        #         f.write(str(x) + '\t' + name + '\t' + code + '\n')




        # for code, name in list(countries):
        #     print(f"{name} ({code})")
        devices = TOTPDevice.objects.filter(user_id=request.user).last()

        if request.POST.get('Reset_2fa') == 'Reset 2FA Device':
            messages.success(request, '2FA Device has been reset.')
            devices.confirmed = True
            devices.save()

        if request.POST.get('save_twofa') == 'Save':
            messages.success(request, 'Account has been updated.')


            devicename = str(request.POST.get('twofa'))

            #print(devicename)
            #print(devices.name)



            # devices = request.POST.get('twofa')
            devices.name = devicename
            #print(devices.name)
            devices.save()


        if request.POST.get('cancel_user') == 'Cancel':
            print('cancel button was triggered')

            #return HttpResponseRedirect('')
            return redirect('account')

        #if request.method == 'POST':
        if request.POST.get('save_user') == 'Save':
            fm = PersonalInfoForm(request.POST, instance=request.user)


            # first_name = request.POST.get('first_name')
            # if fm.is_valid() and first_name != 'Youcef':

            if fm.is_valid():
                messages.success(request, 'Account has been updated.')
                fm.save()
            #else:
                #messages.error(request, 'Neeeeoooo.')
                #context = {"name": request.user, "form": fm}
                #return render(request, 'account.html', context)
                #return HttpResponseRedirect('')
        else:
            fm = PersonalInfoForm(instance=request.user)

        #if request.method == 'POST':
        if request.POST.get('save_password') == 'Save':
            #fm2 = PasswordForm(request.POST, instance=request.user)
            fm2 = SecurityForm(request.user, request.POST)

            # first_name = request.POST.get('first_name')
            # if fm.is_valid() and first_name != 'Youcef':

            if fm2.is_valid():
                messages.success(request, 'Account has been updated.')
                fm2.save()
            # else:
            #     messages.error(request, 'Neeeeoooo.')
            #     context = {"name": request.user, "form2": fm2}
            #     #return render(request, 'account.html', context)
            #     #return HttpResponseRedirect('')
        else:
            fm2 = SecurityForm(request.user)

        # # if request.method == 'POST':
        # if request.POST.get('save_twofa') == 'Save':
        #     # fm2 = PasswordForm(request.POST, instance=request.user)
        #     fm3 = twofaForm(request.user, request.POST)
        #
        #     # first_name = request.POST.get('first_name')
        #     # if fm.is_valid() and first_name != 'Youcef':
        #
        #     if fm3.is_valid():
        #         messages.success(request, 'Account has been updated.')
        #         fm3.save()
        #     # else:
        #     #     messages.error(request, 'Neeeeoooo.')
        #     #     context = {"name": request.user, "form2": fm2}
        #     #     #return render(request, 'account.html', context)
        #     #     #return HttpResponseRedirect('')
        # else:
        #     fm3 = twofaForm(request.user)




        #office = Office.objects.filter(country)
        office = Office.objects.filter(user=request.user)
        #office = Office.objects.only('country_id').filter(user=request.user)
        #office = Office.objects.values_list('country').filter(user=request.user)
        #office = Office.objects.values('country').filter(user=request.user)

        office = Office.objects.values_list('country__name', flat=True).filter(user=request.user)
        devices = TOTPDevice.objects.filter(user_id=request.user).last()


        print(office)

        #context = {"name": request.user, "form": fm, "form2": fm2}
        context = {"name": request.user, "form": fm, "form2": fm2, "office": office, "devices": devices}

        return render(request, 'account.html', context)

    else:
        return redirect('login')









#@axes_dispatch
@check_recaptcha_form
def registerpage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:

            user = form.save(commit=False)
            user.save()

            email_subject = 'WFI Workflow System - User Email Verification'
            email_body = 'verify_email.html'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = generate_user_token.make_token(user)
            to_email = [user.email]

            send_email(user, request, email_subject, email_body, uid, token, to_email)

            messages.success(request, mark_safe(
                'We’ve emailed you instructions to verify your email account, if an account exists with the email you entered.'
                ' <br class="brmedium">If you don’t receive an email, please make sure you’ve entered a valid address when registering, and check your spam folder.</br>'))

            return redirect('register')

    context = {'form': form}
    return render(request, 'register.html', context)




# AJAX
# def load_offices(request):
#     company_role_id = request.GET.get('company_role_id')
#     offices = Office.objects.filter(company_role_id=company_role_id)
#     return render(request, 'office_dropdown_list_options.html', {'offices': offices})
    # return JsonResponse(list(offices.values('id', 'name')), safe=False)



# @axes_dispatch
# @check_recaptcha_login
# def adminloginpage(request, credentials: dict = None):
#
#     attempts_list = get_user_attempts(request, credentials)
#
#     attempt_count = max(
#         (
#                 attempts.aggregate(Sum("failures_since_start"))[
#                     "failures_since_start__sum"
#                 ]
#                 or 0
#         )
#         for attempts in attempts_list
#     )
#     #print(attempt_count)
#
#     attempt_count = attempt_count +1
#
#     adminpage = '/admin/login/'
#
#     context = {'attempt_count': attempt_count, 'adminpage': adminpage}
#
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#
#             if user.is_active and attempt_count <= 3:
#                 if not user.is_staff:
#                     messages.error(request, 'You do not have authorization to access the Admin site.')
#                 login(request, user)
#                 return redirect('/admin/')
#
#             if user.is_active and attempt_count > 3 and request.recaptcha_is_valid:
#                 if not user.is_staff:
#                     messages.error(request, 'You do not have authorization to access the Admin site.')
#                 login(request, user)
#                 return redirect('/admin/')
#
#
#
#             if not user.is_active:
#                 messages.error(request, 'Account for this User has not been Activated.')
#         else:
#             messages.error(request, 'Username or Password is Incorrect.')
#
#     #print(context)
#     return render(request, 'login.html', context)



# @axes_dispatch
# @check_recaptcha_login
# def loginpage(request, credentials: dict = None):
#     form = RegisterForm()
#     attempts_list = get_user_attempts(request, credentials)
#
#     attempt_count = max(
#         (
#                 attempts.aggregate(Sum("failures_since_start"))[
#                     "failures_since_start__sum"
#                 ]
#                 or 0
#         )
#         for attempts in attempts_list
#     )
#     #print(attempt_count)
#
#     attempt_count = attempt_count
#
#     context = {'attempt_count': attempt_count, 'form': form}
#
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#
#             if user.is_active and attempt_count < 3:
#                 login(request, user)
#                 return redirect('home')
#
#             elif user.is_active and request.recaptcha_is_valid:
#                 login(request, user)
#                 return redirect('home')
#
#             if not user.is_active:
#                 messages.error(request, 'Account for this User has not been Activated.')
#         else:
#             messages.error(request, 'Username or Password is Incorrect.')
#
#     #print(context)
#     return render(request, 'login.html', context)



def logoutuser(request):
    logout(request)
    return redirect('login')


# def expiry(request):
#     try:
#         username = request.user.username
#
#         user = User.objects.get(username__exact=username)
#         # start_date = user.date_joined
#
#         now = datetime.datetime.now()
#         print("This is now date:", now)
#         startdate = str(user.start_date)
#         startdate = startdate.rpartition('+')[0]
#         print("This is start date:", startdate)
#
#         startdate = datetime.datetime.fromisoformat(startdate)
#         timedelta = now - startdate
#
#         seconds = timedelta.seconds
#         print("This is seconds:", seconds)
#
#         return seconds
#
#     except Exception as e:
#         return None


def verify_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

        #seconds = expiry(request)


    except Exception as e:
        user = None

    if user and generate_user_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        email_subject = 'WFI Workflow System - User Account Activation'
        email_body = 'activate_account.html'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = generate_admin_token.make_token(user)
        superusers_emails = User.objects.filter(is_superuser=True).values_list('email')

        first_tuple_elements = []

        for a_tuple in superusers_emails:
            first_tuple_elements.append(a_tuple[0])

        superusers_emails = first_tuple_elements

        to_email = superusers_emails

        send_email(user, request, email_subject, email_body, uid, token, to_email)

        messages.success(request, mark_safe(
            'Email verified, the Admin has been notified of your registration and will Approve/Activate your Account shortly.'
            ' <br class="brmedium">You will receive an email once your Account has been Approved.</br>'))
        return redirect('login')

    if user and not generate_user_token.check_token(user, token) and user.is_email_verified:
        messages.info(request, mark_safe(
            'This email address has already been verified for this User.'
            '<br class="brmedium">If you have received a confirmation email of your account being activated, you can go ahead and login, otherwise kindly wait for the activation confirmation email you should receive shortly.</br>'))
        return redirect('login')

    if user and not generate_user_token.check_token(user, token):
        messages.info(request, mark_safe(
            'The email verification link has expired, please re-register an account on the site.'))
        return redirect('register')

    messages.error(request, mark_safe(
        'The Account for this user no longer exists, please re-register an account on the site.'))
    return redirect('register')


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

        #seconds = expiry(request)

    except Exception as e:
        user = None

    if user and generate_admin_token.check_token(user, token):
        user.is_active = True
        user.save()

        email_subject = 'WFI Workflow System - User Account Activated'
        email_body = 'activate_account_confirm.html'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = ''
        to_email = [user.email]

        send_email(user, request, email_subject, email_body, uid, token, to_email)

        messages.add_message(request, messages.SUCCESS,
                             'Account Activated, the User will receive an email notification shortly.')
        return redirect('login')

    if user and not generate_admin_token.check_token(user, token) and user.is_active:
        messages.info(request, mark_safe(
            'This User Account has already been activated.'))
        return redirect('login')

    if user and not generate_admin_token.check_token(user, token) and user.is_email_verified:
        email_subject = 'WFI Workflow System - User Account Activation'
        email_body = 'activate_account.html'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = generate_admin_token.make_token(user)
        superusers_emails = User.objects.filter(is_superuser=True).values_list('email')

        first_tuple_elements = []

        for a_tuple in superusers_emails:
            first_tuple_elements.append(a_tuple[0])

        superusers_emails = first_tuple_elements

        to_email = superusers_emails

        send_email(user, request, email_subject, email_body, uid, token, to_email)

        messages.info(request, mark_safe(
            'Account activation link has expired, a new Activation link has been emailed to the Admins.'
            ' <br class="brmedium">Please ensure you check your spam folder in case email does not appear within your inbox.</br>'))
        return redirect('login')

    messages.error(request, mark_safe(
        'The Account for this user no longer exists, the user will have to re-register an account on the site.'))
    return redirect('login')


class RequestPasswordResetEmail(View):
    #@check_recaptcha_form
    @method_decorator(check_recaptcha_form)
    def get(self, request):
        return render(request, 'password/reset-password.html')

    @method_decorator(check_recaptcha_form)
    def post(self, request):

        email = request.POST['email']

        form = RegisterForm()

        context = {
            'values': request.POST ,'form': form
        }



        current_site = get_current_site(request)

        user = User.objects.filter(email=email)
        user_by_email = User.objects.filter(email=email).first()

        if not user.exists():
            messages.error(request, 'Please supply a valid email')
            return render(request, 'password/reset-password.html', context)

        if user.exists() and request.recaptcha_is_valid:
            uid = urlsafe_base64_encode(force_bytes(user_by_email.pk))
            token = PasswordResetTokenGenerator().make_token(user_by_email)

            email_subject = 'WFI Workflow System - Password Reset'
            email_body = 'password/password_reset_email.html'
            to_email = [user_by_email.email]

            send_email(user, request, email_subject, email_body, uid, token, to_email)

            messages.success(
                request, mark_safe(
                    'We’ve emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly.'
                    '<br class="brmedium"> If you don’t receive an email, please make sure you’ve entered the address you registered with, and check your spam folder.</br>'))

        return render(request, 'password/reset-password.html', context)


class CompletePasswordReset(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(
                    request, 'Password reset link is invalid, please request a new one.')
                return render(request, 'password/reset-password.html')

            if not user:
                messages.info(request, mark_safe(
                    'The Account for this user no longer exists, please re-register an account on the site.'))
                return redirect('register')

        except Exception as identifier:
            messages.info(request, mark_safe(
                'The Account for this user no longer exists, please re-register an account on the site.'))
            return redirect('register')

        return render(request, 'password/set-new-password.html', context)

    @method_decorator(check_recaptcha_form)
    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }

        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'password/set-new-password.html', context)

        if len(password) < 8:
            messages.error(request, 'This password is too short. It must contain at least 8 characters.')
            return render(request, 'password/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            messages.success(
                request, 'Password reset successful, you can go ahead and login with your new password.')
            return redirect('login')
        except Exception as identifier:
            messages.info(
                request, 'Something went wrong, please try again')
            return render(request, 'password/set-new-password.html', context)
