from django.contrib import admin

from home.models import Setting, ContactFormMessage


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Setting)
