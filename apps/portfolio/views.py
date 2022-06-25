from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.portfolio.forms import PortfolioForm, IdentifierForm
from apps.portfolio.models import Identifier, Account
from django.utils import timezone
from stdnum import isin, cusip
from stdnum.gb import sedol
# Create your views here.
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse

import math
import json
from datetime import datetime


def portfolios(request):

    if request.user.is_authenticated:

        #account = Account.objects.filter(username=request.user)

        #print(request.user)
        #print(account)

        #if request.method == 'POST':
        if request.POST:
            fm = PortfolioForm(request.POST)
            fm2 = IdentifierForm(request.POST)


            if fm.is_valid() and fm2.is_valid():
                messages.success(request, 'Portfolio has been created.')


                # identifier_type = fm.cleaned_data.get("identifier_type")
                # identifier_type = str(identifier_type)
                #
                # print(identifier_type)


                #identifier = fm2.save(commit=False)

                identifier = fm2.cleaned_data['code']
                identifier_list = identifier.splitlines()
                isin_list = []
                uscode_list = []
                sedol_list = []
                invalid_list = []
                counter = 0
                #ids = []

                for line in identifier_list:

                    if line not in isin_list and line not in uscode_list and line not in sedol_list and line not in invalid_list and line != '':

                        val_isin = isin.is_valid(line)
                        val_uscode = cusip.is_valid(line)
                        val_sedol = sedol.is_valid(line)

                        # if identifier_type == 'ISIN':
                        if len(line) == 12 and val_isin is True:


                            #if val_isin is True:
                                #print("Identifier: " + str(line), 'Valid')
                            #counter = counter + 1
                            #isin_list.append(counter)
                            isin_list.append(line)

                            #ids.append(counter)


                            #else:
                                #print("Identifier: " + str(line), 'Neeeeeooooo')
                                #invalid_list.append(line)

                        # elif identifier_type == 'USCODE':

                        elif len(line) == 9 and val_uscode is True:

                            #val_uscode = cusip.is_valid(line)

                            #if val_uscode is True:
                                # print("Identifier: " + str(line), 'Valid')
                            #counter = counter + 1
                            uscode_list.append(line)

                            #ids.append(counter)

                        elif len(line) == 7 and val_sedol is True:

                            #val_uscode = cusip.is_valid(line)

                            #if val_uscode is True:
                                # print("Identifier: " + str(line), 'Valid')
                            #counter = counter + 1
                            sedol_list.append(line)

                            #ids.append(counter)

                        else:
                            #print("Identifier: " + str(line), 'Neeeeeooooo')

                            #counter = counter + 1
                            invalid_list.append(line)

                            #ids.append(counter)


                #print("Valid List of Identifiers: ", isin_list, uscode_list, sedol_list)
                #print("Invalid List of Identifiers: ", invalid_list)

                print('Validation complete')


                # Account.objects.username = request.user
                portfolio = fm.save(commit=False)
                portfolio.user = request.user
                portfolio.actflag = 'I'

                isin_count = len(isin_list)
                uscode_count = len(uscode_list)
                sedol_count = len(sedol_list)
                valid_count = isin_count + uscode_count + sedol_count
                invalid_count = len(invalid_list)

                portfolio.isin_count = isin_count
                portfolio.uscode_count = uscode_count
                portfolio.sedol_count = sedol_count

                portfolio.initial = isin_count + uscode_count + sedol_count + invalid_count
                portfolio.total = isin_count + uscode_count + sedol_count + invalid_count

                portfolio.valid = valid_count
                portfolio.invalid = invalid_count


                portfolio.save()



                # use this

                print('Loading to DB')

                Identifier.objects.bulk_create([Identifier(code_type='ISIN', code=x, actflag='I', account=portfolio, valid=True)
                                          for x in isin_list], batch_size=10000)

                Identifier.objects.bulk_create([Identifier(code_type='USCODE', code=x, actflag='I', account=portfolio, valid=True)
                                          for x in uscode_list], batch_size=10000)

                Identifier.objects.bulk_create([Identifier(code_type='SEDOL', code=x, actflag='I', account=portfolio, valid=True)
                                          for x in sedol_list], batch_size=10000)



                Identifier.objects.bulk_create([Identifier(code=x, actflag='I', account=portfolio)
                                          for x in invalid_list], batch_size=10000)

                fm.save()

                print('DB Load Complete')


            else:
                messages.error(request, 'Please ensure you enter at least one Identifier within the Portfolio text input box.')
                context = {"name": request.user, "form": fm, "form2": fm2}
                return render(request, 'portfolios.html', context)

            return redirect('portfolios')
        else:
            fm = PortfolioForm()
            fm2 = IdentifierForm()
            account = Account.objects.filter(user=request.user)

            page = request.GET.get('page', 1)
            paginator = Paginator(account, 3)

            try:
                portfolios = paginator.page(page)
            except PageNotAnInteger:
                portfolios = paginator.page(1)
            except EmptyPage:
                portfolios = paginator.page(paginator.num_pages)



        #context = {"name": request.user, "form": fm, "form2": fm2}
        context = {"name": request.user, "form": fm, "form2": fm2, "account": account, "page": page, "portfolios": portfolios}

        print('Process Finished')

        return render(request, 'portfolios.html', context)



    else:
        return redirect('login')


def portfolio(request, pk):
    portfolio = Account.objects.get(id=pk)
    identifiers = Identifier.objects.filter(account=pk)
    context = {"portfolio": portfolio, "identifiers": identifiers}

    return render(request, 'portfolio.html', context)


def portfolio_json(request, pk):
    portfolio = Account.objects.get(id=pk)

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    _search = request.GET.get('search[value]')
    _orderType = request.GET.get('order[0][dir]')

    _orderField = request.GET.get('order[0][column]')

    if _orderField == '0':
        _orderField = '1'
    _orderField = 'columns[' + _orderField + '][data]'
    _orderField = request.GET.get(_orderField)
    identifiers = Identifier.objects.filter(account=pk)
    identifiers = identifiers.filter(code__contains=_search)

    if _orderType == 'desc':
        identifiers = identifiers.order_by(_orderField)

    else:
        _orderField = '-' + _orderField
        identifiers = identifiers.order_by(_orderField)

    total = identifiers.count()
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1
        per_page = length

        identifiers = identifiers[start:start+length]

    data = [identifier.get_data() for identifier in identifiers]
    response = {
        'data': data,
        'page': page,
        'per_page': per_page,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)


def deletePortfolio(request, pk):
    portfolio = Account.objects.get(id=pk)
    portfolio.delete()
    return redirect('portfolios')


def deleteIdentifier(request, pk):
    if request.method == 'POST':
        identifier = Identifier.objects.get(id=pk)
        identifier.delete()
        
        portfolio = Account.objects.get(id=identifier.account_id)

        portfolio.update = portfolio.total - 1
        portfolio.total = portfolio.total - 1
        if identifier.valid:
            portfolio.valid = portfolio.valid - 1
        else:
            portfolio.invalid = portfolio.invalid - 1
        if identifier.code_type == 'ISIN':
            portfolio.isin_count = portfolio.isin_count - 1
        elif identifier.code_type == 'USCODE':
            portfolio.uscode_count = portfolio.uscode_count - 1
        elif identifier.code_type == 'SEDOL':
            portfolio.sedol_count = portfolio.sedol_count - 1
        portfolio.save()
    return JsonResponse({'data': 'success'})


def updateIdentifier(request, pk):
    if request.method == 'POST':
        updateDataIdentifier(request.POST['code'], request.POST['code_type'], pk)
    return JsonResponse({'data': 'success'})


def updateDataIdentifier(code, code_type, pk):
    identifier = Identifier.objects.get(id=pk)
    identifier.code = code
    identifier.code_type = code_type
    identifier.updated = datetime.now()
    identifier.save()


def insertIdentifier(request):
    code = request.POST['code']
    code_type = request.POST['code_type']
    account_id = request.POST['account_id']
    portfolio = Account.objects.get(id=account_id)

    identifier = Identifier.objects.create(
        code=code, code_type=code_type, account=portfolio
    )
    identifier.save()

    portfolio.total = portfolio.total + 1
    if identifier.valid:
        portfolio.valid = portfolio.valid + 1
    else:
        portfolio.invalid = portfolio.invalid + 1
    if identifier.code_type == 'ISIN':
        portfolio.isin_count = portfolio.isin_count + 1
    elif identifier.code_type == 'USCODE':
        portfolio.uscode_count = portfolio.uscode_count + 1
    elif identifier.code_type == 'SEDOL':
        portfolio.sedol_count = portfolio.sedol_count + 1
    portfolio.save()

    return JsonResponse({'data': 'success'})


def bulk_delete(reqeust):
    delete_ids = reqeust.POST['delete_ids']
    delete_ids = json.loads(delete_ids)
    for i, id in enumerate(delete_ids):
        if id != '':
            success = deleteIdentifier(reqeust, id)
    return JsonResponse({'data': 'success'})


def bulk_edit(request):
    edit_ids = request.POST['edit_ids']
    code = request.POST['code']
    code_type = request.POST['code_type']
    edit_ids = json.loads(edit_ids)
    for i, id in enumerate(edit_ids):
        if id != '':
            updateDataIdentifier(code, code_type, id)
    return JsonResponse({'data' : 'success'})
