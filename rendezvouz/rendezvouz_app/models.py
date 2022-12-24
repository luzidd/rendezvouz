from django.db import models

# Create your models here.
class user(models.Model):
    display_name = models.CharField(max_length=32)
    e_mail = models.CharField(max_length=50)
    auth = models.CharField(max_length=64)

class event(models.Model):
    host = models.ForeignKey(user)
    members = models.ManyToManyField(user)