from django.db import models
from django.contrib.auth.models import User

class Mechanic(models.Model):
    user = models.ForeignKey(User)

class Vehicle(models.Model):
    user = models.ForeignKey(User)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    registration_no = models.CharField(max_length=30)
    
class BreakdownCover(models.Model):
    start_date = models.DateField() 
    end_date = models.DateField()
    user = models.ForeignKey(User)
    
class Job(models.Model):
    user = models.ForeignKey(User)
    