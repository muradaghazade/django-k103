from django.contrib import admin
from core.models import News
from django.contrib.auth.models import Group

admin.site.register(News)
admin.site.unregister(Group)