from django import forms
from .models import Trip, Activity
from django.contrib.auth.models import User
from .import models

class TripModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['admin', 'users']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'})
        }

class ActivityModelForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['user', 'trip']
        widgets = {
            'start_time': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.TextInput(attrs={'type': 'datetime-local'})
        }

class TripUsersModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['users']
        
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        