from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from datetimeutc.fields import DateTimeUTCField

class Merch(models.Model):
    ID          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200)
    
    description = models.CharField(max_length=500)  
    upc         = models.IntegerField()
    in_stock    = models.BooleanField(default=False)
    timestamp   = DateTimeUTCField(auto_now_add=True)

    def __str__(self):
        return self.ID 