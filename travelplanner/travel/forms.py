from django import forms
from .models import Trip

class TripModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['admin']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'})
        }