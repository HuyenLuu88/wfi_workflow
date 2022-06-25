from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django_otp.decorators import otp_required
from apps.account.models import User, CompanyRole, Office, Country
# @otp_required(login_url='login')
from django_otp.models import DeviceManager, Device
from django_otp.plugins.otp_totp.models import TOTPDevice
from apps.account.forms import RegisterForm, PersonalInfoForm, SecurityForm #, twofaForm
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.safestring import mark_safe
from django.contrib import messages
import json
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.http import JsonResponse
from apps.product.models import Wca
from apps.portfolio.models import Identifier, Account
from apps.task.models import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):

    #wca = Wca.objects.get(id=1)

    #identifiers = Identifier.objects.filter(code=Wca.isin)

    #account = Account.objects.filter(username=request.user)
    account = Account.objects.filter(user=request.user)[:3]

    #identifiers = Wca.objects.get[:10]
    wca = Wca.objects.all()[:5000]
    #portfolio = Identifier.objects.filter(code=Wca.code)

    #for item in identifiers:
    #print(wca.secid)

    feed = Feed.objects.all()[:50]

    page = request.GET.get('page', 1)
    paginator = Paginator(wca, 10)

    try:
        wca_identifiers = paginator.page(page)
    except PageNotAnInteger:
        wca_identifiers = paginator.page(1)
    except EmptyPage:
        wca_identifiers = paginator.page(paginator.num_pages)

    feed = Feed.objects.all()[:50]

    # page = request.GET.get('page', 1)
    # paginator = Paginator(feed, 10)
    #
    # try:
    #     wca_tasks = paginator.page(page)
    # except PageNotAnInteger:
    #     wca_tasks = paginator.page(1)
    # except EmptyPage:
    #     wca_tasks = paginator.page(paginator.num_pages)


    context = {"account": account, "wca": wca, "page": page, "wca_identifiers": wca_identifiers, "feed": feed}


    return render(request, 'dashboard.html', context)





# def tasks(request):
#     return render(request, 'tasks.html')

# def task1(request):
#     return render(request, 'tasks/task1.html')


def knowledgebase(request):
    return render(request, 'knowledgebase.html')





def test(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"name": request.user, "form": form}

    return render(request, 'test.html', context)



# AJAX
def load_offices(request):
    company_role_id = request.GET.get('company_role_id')
    offices = Office.objects.filter(company_role_id=company_role_id)
    return render(request, 'office_dropdown_list_options.html', {'offices': offices})
    # return JsonResponse(list(offices.values('id', 'name')), safe=False)







def test2(request):
    return render(request, 'test2.html')


def clocks(request):
    return render(request, 'clocks.html')




