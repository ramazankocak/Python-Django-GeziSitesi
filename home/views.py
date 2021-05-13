from django.http import HttpResponse

def index(request):
    text="MerHaBa"
    return HttpResponse("DosTuM %s" % text)