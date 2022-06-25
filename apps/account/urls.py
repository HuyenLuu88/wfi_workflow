from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views
from .views import RequestPasswordResetEmail, CompletePasswordReset
# from .forms import EmailValidationOnForgotPassword
# from apps.account.views import loginpage
from .forms import RegisterForm

urlpatterns = [
    path('account/', views.account, name="account"),
    path("account/login/", auth_views.LoginView.as_view(template_name="two_factor/core/login.html", form_class=RegisterForm), name="login", ),
    # path('login/', loginpage.as_view(), name="login"),
    # path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registerpage, name="register"),
    path('verify-email/<uidb64>/<token>', views.verify_email, name="verify_email"),
    path('activate-account/<uidb64>/<token>', views.activate_account, name="activate_account"),

    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(), name="reset-user-password"),

    path("request-reset-link/", RequestPasswordResetEmail.as_view(), name="request-password"),
]
