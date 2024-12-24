from django.contrib import admin
from core.models import News, Car, Video, Comp
from django.contrib.auth.models import Group

admin.site.register(News)
admin.site.register(Car)
admin.site.register(Video)
admin.site.unregister(Group)
admin.site.register(Comp)