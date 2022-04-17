from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import *
from django.template import loader


def index(request):
    template = loader.get_template('statsviewers/index.html')
    data = {}
    return HttpResponse(template.render(data, request))
