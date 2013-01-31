from django.db import models
from django.contrib.auth.models import User

class Mechanic(models.Model):
    user = models.ForeignKey(User)
    
class Cover(models.Model):
    name = models.CharField(max_length=20)
    
class Job(models.Model):
    user = models.ForeignKey(User)
    