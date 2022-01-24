from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from datetimeutc.fields import DateTimeUTCField

class Release(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=500)       
    artist = models.CharField(max_length=500)  
    release_blurb = models.CharField(max_length=500)  
    release_date = DateTimeUTCField()
    timestamp = DateTimeUTCField(auto_now_add=True)
    def __str__(self):
        return self.ID 
