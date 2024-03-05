from django.contrib import admin
from .models import Trip, Activity, TripUsers

admin.site.register(Trip)
admin.site.register(Activity)
admin.site.register(TripUsers)