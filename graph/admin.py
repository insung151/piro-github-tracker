from django.contrib import admin
from django.contrib.auth import models
from .models import *


class ContribAdmin(admin.ModelAdmin):
    list_display = ('member', 'level', 'date',)
    list_per_page = 50
    list_filter = ['member']


class MemberAdmin(admin.ModelAdmin):
    list_display = ('github_username', 'updated_at')

    def updated_at(self, member):
        if __name__ == '__main__':
            return str(member.logs.objects.last())


admin.site.register(Member)
admin.site.register(Contrib, ContribAdmin)
