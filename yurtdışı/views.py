from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    text="Uzak diyarlar"
    return HttpResponse("%s a gitmek istiyorum. " %text)