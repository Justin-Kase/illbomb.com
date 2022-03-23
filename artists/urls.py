from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.artists, name='index'),
    path('artists/', views.artists, name='artists'),
    
    re_path(r'^artists/(?P<pk>[0-9]+)$', views.artist_detail),

    re_path(r'^api/artists$', views.artists),
    re_path(r'^api/artists/(?P<pk>[0-9]+)$', views.artist_detail),
    re_path(r'^api/artists/timestamp$', views.artist_list_created),
]   