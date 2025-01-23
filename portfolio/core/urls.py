from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:id>/',news_detail, name='news_detail'),
    path('cars/', cars, name='cars'),
    path('car/<int:id>/', car, name='car'),
    path('videos/', videos, name='videos'),
    path('video/<int:id>/', video, name='video'),
    path('comp/', comp, name='comp'),
    path('comps/<int:id>/', comps, name='comps'),
    path('create-news/', create_news, name='create_news'),
]