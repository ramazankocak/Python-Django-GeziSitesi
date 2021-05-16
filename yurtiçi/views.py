from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text="TÜRKİYE"
    return HttpResponse("%s 'yi gez öncelikle." % text)