from django.contrib import admin

from yurtiçi.models import Bölge, Şehirler


class BölgeAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class ŞehirlerAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','bölge']
    list_filter = ['status']

admin.site.register(Bölge,BölgeAdmin)
admin.site.register(Şehirler,ŞehirlerAdmin)