from django.http import Http404, HttpResponse
from .models import *
from django.template import loader


def index(request):
    template = loader.get_template('statsviewers/index.html')
    data = {}
    return HttpResponse(template.render(data, request))


def tracks(request):
    template = loader.get_template('statsviewers/tracklist.html')
    alltracks = Cup.objects.all()
    data = {'itemList':alltracks}
    return HttpResponse(template.render(data, request))

def builds(request):
    template = loader.get_template('statsviewers/buildlist.html')
    allbuilds = Build.objects.all()
    print('DEBUG')
    print('DEBUG')
    print('DEBUG')
    print(allbuilds)
    data = {'itemList':allbuilds}
    return HttpResponse(template.render(data, request))