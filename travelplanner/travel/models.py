from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length = 100)
    admin = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'trip_admin')
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User)

class Activity(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length = 100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    link = models.URLField()
    
class TripUsers(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

