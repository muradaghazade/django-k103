from django.shortcuts import render
from core.models import News, Car

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
    context = {
        'car': car
    }
    return render(request, 'car-detail.html', context)