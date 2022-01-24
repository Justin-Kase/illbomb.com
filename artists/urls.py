from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.artists, name='index'),
    path('artists/', views.artists, name='artists'),
]    
   