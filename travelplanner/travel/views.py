from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Trip
from .forms import TripModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    user = request.user
    return render(request, 'travel/home.html',{'message':"Boom message!", 'user': user.username})

class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripModelForm
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    success_url = 'home'
    # TODO date validation: end date > start date