from django.contrib import admin

from yurtiçi.models import Bölge, Şehirler, Images

class ŞehirlerImageInline(admin.TabularInline):
    model = Images
    extra = 3

class BölgeAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class ŞehirlerAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','bölge','image_tag']
    list_filter = ['status']
    inlines = [ŞehirlerImageInline]
    readonly_fields = ('image_tag',) #models.py deki image_tag
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','image',]

admin.site.register(Bölge,BölgeAdmin)
admin.site.register(Şehirler,ŞehirlerAdmin)
admin.site.register(Images,ImagesAdmin)