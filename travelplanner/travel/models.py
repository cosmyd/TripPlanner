from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length = 100)
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Activity(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length = 100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    link = models.URLField()
    
class TripUsers(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

