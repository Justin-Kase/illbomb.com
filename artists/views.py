import tempfile
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status 
from artists.models import Artist
from rest_framework import viewsets
from rest_framework import permissions
from artists.serializers import ArtistSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    artist_data = Artist.objects.all()

    artist_data_dict = {
        'artist_data': artist_data
    }
    return render(request, 'artists.html', artist_data_dict)

def artists(request):
    artist_data = Artist.objects.all()

    artist_data_dict = {
        'artist_data': artist_data
    }
    return render(request, 'artists.html', artist_data_dict)

def artists_list(request):
    artist_data = Artist.objects.all()

    artist_data_dict = {
        'artist_data': artist_data
    }
    return render(request, 'artists.html', artist_data_dict)   

def artist_detail(request):
    artist_data = Artist.objects.get(request)

    artist_data_dict = {
        'artist_data': artist_data
    }
    return render(request, 'artists.html', artist_data_dict)    

def artist_list_created(request):
    artist_data = Artist.objects.all()

    artist_data_dict = {
        'artist_data': artist_data
    }
    return render(request, 'artists.html', artist_data_dict)     