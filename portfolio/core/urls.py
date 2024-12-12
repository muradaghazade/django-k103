from django.urls import path
from core.views import home, cars, car

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('cars/', cars, name='cars'),
    path('car/<int:id>/', car, name='car'),
]