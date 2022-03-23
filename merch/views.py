import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from merch.models import Merch
from django.views.generic import TemplateView

def index(request):
    merch_data = Merch.objects.all()
    merch_data_dict = {
        'merch_data': merch_data
    }

    return render(request, 'merch.html', merch_data_dict)

def merch(request):
    merch_data = Merch.objects.all()
    merch_data_dict = {
        'merch_data': merch_data
    }

    return render(request, 'merch.html', merch_data_dict)