from django.urls import path
from core.views import home, cars, car, news_detail

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:id>/',news_detail, name='news_detail'),
    path('cars/', cars, name='cars'),
    path('car/<int:id>/', car, name='car'),
]