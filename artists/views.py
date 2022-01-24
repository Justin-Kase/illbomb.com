import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist

from django.views.generic import TemplateView


def index(request):
    artist_data = Artist.objects.all()
    #return HttpResponse('index.html')

    artist_data_dict = {
        'artist_data': artist_data
    }

    return render(request, 'artists.html', artist_data_dict)


def artists(request):
    artist_data = Artist.objects.all()
    #return HttpResponse('index.html')

    artist_data_dict = {
        'artist_data': artist_data
    }

    return render(request, 'artists.html', artist_data_dict)
