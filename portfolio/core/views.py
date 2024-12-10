from django.shortcuts import render
from core.models import News, Author

def home(request):
    news = News.objects.all()
    context = {
        'xeberler': news
    }
    return render(request, 'index.html', context)



def authors(request):
    news = News.objects.all()
    context = {
        'xeberler': news
    }
    return render(request, 'index.html', context)