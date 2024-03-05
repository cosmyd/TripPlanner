from django import forms
from .models import Trip, Activity

class TripModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['admin']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'})
        }

class ActivityModelForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['user', 'trip']
        widgets = {
            'start_time': forms.TextInput(attrs={'type': 'time'}),
            'end_time': forms.TextInput(attrs={'type': 'time'})
        }
