from django.shortcuts import render, redirect
from core.models import News, Car, Video, Comp
from core.forms import *

def home(request):
    search = request.GET.get('search')
    news = News.objects.order_by('-id')
    if search:
        news = News.objects.filter(title__icontains=search)
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


def video(request, id):
    video = Video.objects.get(id=id)
    video.views += 1
    video.save()
    context = {
        'video': video
    }
    return render(request, 'video-detail.html', context)

def comp(request):
    comp = Comp.objects.all()
    context = {
        'comp': comp
    }
    return render(request, 'comp-elan.html', context)


def comps(request, id):
    comps = Comp.objects.get(id=id)
    context = {
        'comps': comps
    }
    return render(request, 'comp-details.html', context)


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('core:home')
    form = NewsForm()
    return render(request, 'create-news.html', {'form':form})