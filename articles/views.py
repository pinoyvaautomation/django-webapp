#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Article, Category
from shop.models import Product
from download_library.models import Customer, File
from django.db.models import Q # type: ignore
from django.http import HttpResponse, JsonResponse # type: ignore

def HomePage(request):
    return render(request, 'master.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list_template.html', {'articles': articles})
    #return render(request, 'main.html', {'articles': articles})

    #return render(request, 'article_list.html')
    
    #return HttpResponse('Homepage')

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail_template.html', {'article': article})


def article_search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        articles = Article.objects.none()
    return render(request, 'article_search.html', {'articles': articles, 'query': query})

#SEARCH QUERY

def search_articles(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })


def ajax_search_articles(request):
    query = request.GET.get('q', '')
    #results = []
    data = {
        'articles': [],
        'products': [],
        'customers': []
    }

    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

        customers = Customer.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )

        data['articles'] = [
            {'id': a.id, 'title': a.title, 'snippet': a.content[:100]} for a in articles
        ]

        data['products'] = [
            {'id': p.id, 'name': p.name, 'desc': p.description[:100]} for p in products
        ]

        data['customers'] = [
            {'id': c.id, 'name': c.name, 'desc': c.email[:100]} for c in customers
        ]

    return JsonResponse(data)
