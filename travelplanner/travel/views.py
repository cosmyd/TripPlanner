from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Trip
from .forms import TripModelForm, ActivityModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    user = request.user
    return render(request, 'travel/home.html',{'message':"Boom message!", 'user': user.username})

class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripModelForm
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    success_url = '/'
    # TODO date validation: end date > start date

class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip


#Don't forget mixins are just some classes you inherit some methods from from (ex the test_func we override)
class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Trip
    form_class = TripModelForm
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    success_url = '/'

    def test_func(self):
        trip = self.get_object()
        if self.request.user == trip.admin:
            return True
        
        else:
            return False


class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trip
    success_url = '/'

    def test_func(self):
        trip = self.get_object()
        if self.request.user == trip.admin:
            return True
        
        else:
            return False



def add_activity(request, trip_pk):
    trip = get_object_or_404(Trip, pk = trip_pk)
    user = request.user
    if trip.admin != user:
        return HttpResponse('You are trying to access another user\'s trip ')
    if request.method == 'POST':
        form = ActivityModelForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = user
            activity.trip = trip
            activity.save()
            return redirect('trip-detail', pk = trip_pk)
    else:
        form = ActivityModelForm()
    return render(request, 'travel/add_activity.html', {'form': form, 'trip': trip})