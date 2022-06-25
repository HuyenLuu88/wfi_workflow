"""wfi_workflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .views import test
from apps.account import views as adminviews
from two_factor.urls import urlpatterns as tf_urls
#from two_factor.admin import AdminSiteOTPRequired
from apps.account.forms import RegisterForm
#admin.site.__class__ = AdminSiteOTPRequired
from django_otp.admin import OTPAdminSite



admin.site.__class__ = OTPAdminSite




urlpatterns = [
    #path('admin/login/', adminviews.adminloginpage),


    path('admin/', admin.site.urls),
    path('', include(tf_urls)),
    path('', include('apps.account.urls')),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.product.urls')),
    path('', include('apps.task.urls')),
    path('', views.home, name="home"),
    #path('tasks/', views.tasks, name="tasks"),
    #path('tasks/task1/', views.task1, name="task1"),
    path('knowledgebase/', views.knowledgebase, name="knowledgebase"),

    path('test/', views.test, name="test"),


    path('test2/', views.test2, name="test2"),
    path('clocks/', views.clocks, name="clocks"),
    path('chaining/', include('smart_selects.urls')),
    # path('ajax/load-offices/', views.load_offices, name='ajax_load_offices'), # AJAX



    # path('account/', include('django.contrib.auth.urls')),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html", success_url='password/password_reset_confirm.html'), name='password_reset_confirm'),


    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html', success_url="/login/" ), name="password_reset_confirm"),

    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
