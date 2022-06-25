from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.task.models import Identifier, Feed
# Create your views here.
# def tasks(request):
#     return render(request, 'tasks.html')

def tasks(request):

    #wca = Wca.objects.get(id=1)

    #identifiers = Identifier.objects.filter(code=Wca.isin)

    #account = Account.objects.filter(username=request.user)
    #account = Feed.objects.filter(username=request.user)[:3]

    #identifiers = Wca.objects.get[:10]
    feed = Feed.objects.all()[:50]
    #portfolio = Identifier.objects.filter(code=Wca.code)

    #for item in identifiers:
    #print(wca.secid)

    page = request.GET.get('page', 1)
    paginator = Paginator(feed, 10)

    try:
        wca_feed = paginator.page(page)
    except PageNotAnInteger:
        wca_feed = paginator.page(1)
    except EmptyPage:
        wca_feed = paginator.page(paginator.num_pages)

    context = {"page": page, "wca_feed": wca_feed}


    return render(request, 'tasks.html', context)
