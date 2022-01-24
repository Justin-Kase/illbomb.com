from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.releases, name='index'),
    path('releases/', views.releases, name='releases'),
]    
   