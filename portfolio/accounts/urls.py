from django.urls import path
from accounts.views import register, login, profile
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:id>/', profile, name='profile'),
]
