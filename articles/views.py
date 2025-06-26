#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Article, Category
from django.db.models import Q # type: ignore
from django.http import HttpResponse # type: ignore

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
