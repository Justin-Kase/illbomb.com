from django.contrib.auth.models import User, Group
from django import views
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static


from artists.views import ArtistViewSet, GroupViewSet, UserViewSet
from illbomb.views import index
from rest_framework import routers, serializers, viewsets 


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)    
router.register(r'artists', ArtistViewSet)  

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls), 
    #=======================================================
    path('', index),  
    path('artists/', include('artists.urls')),
    path('releases/', include('releases.urls')),
    path('merch/', include('merch.urls')),
    path('summernote/', include('django_summernote.urls')) ,
    re_path(r'^', include('artists.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)