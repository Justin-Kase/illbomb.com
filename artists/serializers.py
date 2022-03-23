from rest_framework import serializers 
from django.contrib.auth.models import User, Group
from artists.models import Artist
  
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('url',
                  'ID',
                  'name',
                  'bio',
                  'headshot',
                  'website',
                  'timestamp')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']                 