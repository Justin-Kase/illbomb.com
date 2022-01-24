from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls), 
    #=======================================================
    path('', index),  
    path('artists/', include('artists.urls')),
    path('releases/', include('releases.urls')),
    path('summernote/', include('django_summernote.urls')) ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)