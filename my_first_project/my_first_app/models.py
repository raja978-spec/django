from django.db import models


class FirstModel(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=14, null=True)
    joined_date = models.DateTimeField(auto_now=True, null=True)
    
