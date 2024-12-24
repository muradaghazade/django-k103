from django.shortcuts import render
from core.models import News, Car, Video

def home(request):
    news = News.objects.all()
    context = {
        'xeberler': news
    }
    return render(request, 'index.html', context)



def cars(request):
    cars = Car.objects.order_by('-id')
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context)


def car(request, id):
    car = Car.objects.get(id=id)
    car.views += 1
    car.save()
    context = {
        'car': car
    }
    return render(request, 'car-detail.html', context)

def news_detail(request, id):
    news = News.objects.get(id=id)
    news.views += 3
    news.save()
    context = {
        'news': news
    }
    return render(request, 'news-detail.html', context)


def videos(request):
    vids = Video.objects.all()
    context = {
        'videos': vids
    }
    return render(request, 'videos.html', context)