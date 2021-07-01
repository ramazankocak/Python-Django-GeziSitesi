from django.core.mail import message
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactFormMessage
from yurtiçi.models import Şehirler


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Şehirler.objects.all()[:3]
    context={'setting':setting, 'page':'home','sliderdata':sliderdata}
    return render(request, 'index.html',context)
def iletisim(request):
    if request.method == 'POST':
        form = ContactFormMessage(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            message.success(request, "Mesajınız başarı ile gönderilmiştir.Teşekkür Ederiz.")
            return HttpResponseRedirect ('/iletisim')

    setting=Setting.objects.get(pk=1)
    context={'setting':setting, 'form':'form'}
    return render(request, 'iletisim.html',context)
def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'hakkimizda.html',context)
def referanslar(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'referanslar.html',context)