from django.db import models
class Info(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)