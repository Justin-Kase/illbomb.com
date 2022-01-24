from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Artist(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)   
    headshot = models.CharField(max_length=500)  
    website = models.CharField(max_length=500)  
    timestamp = models.CharField(max_length=200)
 
    def __str__(self):
        return self.ID 