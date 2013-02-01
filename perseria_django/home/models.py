from django.db import models
from django.contrib.auth.models import User

class Mechanic(models.Model):
    user = models.ForeignKey(User)
    
class Vehicle(models.Model):
    user = models.ForeignKey(User)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    registration_no = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.registration_no
    
class Cover(models.Model):
    BASIC = 'Basic'
    EXTENDED = 'Extended'
    CHOICES = ((BASIC, 'Basic'), (EXTENDED, 'Extended'))
    type = models.CharField(max_length = 20, choices=CHOICES, default=BASIC)
    description = models.TextField()
    cost = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.type

class BreakdownCover(models.Model):
    cover = models.ForeignKey(Cover)
    start_date = models.DateField() 
    end_date = models.DateField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.user.username
    
class Job(models.Model):
    user = models.ForeignKey(User)
    