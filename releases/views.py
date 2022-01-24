import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from .models import Release
from django.views.generic import TemplateView

def index(request):
    release_data = Release.objects.all()
    release_data_dict = {
        'release_data': release_data
    }

    return render(request, 'releases.html', release_data_dict)

def releases(request):
    release_data = Release.objects.all()
    release_data_dict = {
        'release_data': release_data
    }

    return render(request, 'releases.html', release_data_dict)