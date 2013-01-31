from django.db import models
from django.contrib.auth.models import User

class Mechanics(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    
class Cover(models.Model):
    name = models.CharField()