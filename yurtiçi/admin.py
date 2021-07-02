from django.contrib import admin

from yurtiçi.models import Bölge, Şehirler, Images
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

class ŞehirlerImageInline(admin.TabularInline):
    model = Images
    extra = 3

class BölgeAdmin(MPTTModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class ŞehirlerAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','bölge','image_tag']
    list_filter = ['bölge','status']
    inlines = [ŞehirlerImageInline]
    readonly_fields = ('image_tag',) #models.py deki image_tag
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','image',]

class BölgeAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Add cumulative product count
        qs = Bölge.objects.add_related_count(
                qs,
                Şehirler,
                'bölge',
                'products_cumulative_count',
                cumulative=True)
        # Add non cumulative product count
        qs = Bölge.objects.add_related_count(qs,
                 Şehirler,
                 'bölge',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(Bölge,BölgeAdmin2)
admin.site.register(Şehirler,ŞehirlerAdmin)
admin.site.register(Images,ImagesAdmin)