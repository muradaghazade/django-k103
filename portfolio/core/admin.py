from django.contrib import admin
from core.models import News, Car
from django.contrib.auth.models import Group

admin.site.register(News)
admin.site.register(Car)
admin.site.unregister(Group)