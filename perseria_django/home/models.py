from django.db import models
from django.contrib.auth.models import User

class Mechanics(models.Model):
    user = models.ForeignKey(User)