from django.contrib import admin
from django.contrib.auth import models
from .models import *


class ContribAdmin(admin.ModelAdmin):
    list_display = ('member', 'level', 'date', )
    list_per_page = 50
    list_filter = ['member']


admin.site.register(Member)
admin.site.register(Contrib, ContribAdmin)
