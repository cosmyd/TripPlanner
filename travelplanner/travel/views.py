from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Trip, Activity
from .forms import TripModelForm, ActivityModelForm, TripUsersModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from users.models import FriendRequest
import datetime


def home(request):
    user = request.user
    return render(request, 'travel/home.html',{'message':"Boom message!", 'user': user.username})

@login_required
def dashboard(request):
    user = request.user
    now = datetime.datetime.now()
    upcoming_trips = Trip.objects.filter(Q(start_date__gt = now) & (Q(admin = user) | Q(users = user)))
    friend_requests = FriendRequest.objects.filter(to_user = user)
    current_trips = Trip.objects.filter(Q(start_date__gt = now) & Q(start_date__lt = now) & Q(end_date__gt = now))

    context = {
        'trips': upcoming_trips,
        'current_trips': current_trips,
        'friend_requests' : friend_requests
    }
    return render(request, 'travel/dashboard.html', context)


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activity.objects.filter(trip = self.get_object())
        return context

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

@login_required
def trip_users(request, trip_pk):
    trip = get_object_or_404(Trip, pk = trip_pk)
    user = request.user
    if trip.admin != user:
        return HttpResponse('You are trying to modify another user\'s trip ')
    if request.method == 'POST':
        form = TripUsersModelForm(request.POST, trip_admin = trip.admin)
        ### TODO prepopulate the trip users many to many field

        if form.is_valid():
            trip.users.clear()
            users_to_add = form.cleaned_data['users']
            for user in users_to_add:
                trip.users.add(user.id)
            trip = trip.save()
            return redirect('trip-detail', pk = trip_pk)
    else:
        form = TripUsersModelForm(trip_admin = trip.admin)

    return render(request, 'travel/trip_users_form.html', {'form': form, 'trip': trip})


def add_activity(request, trip_pk):
    trip = get_object_or_404(Trip, pk = trip_pk)
    user = request.user
    trip_users = trip.users.all()
    if trip.admin != user and user not in trip_users:
        return HttpResponse('You are trying to modify another user\'s trip ')
    if request.method == 'POST':
        form = ActivityModelForm(request.POST)
        if form.is_valid():   
            activity = form.save(commit=False)
            activities = Activity.objects.filter(trip = trip)
            ok = True           
            for activity_it in activities:
                if activity.start_time < activity_it.end_time and activity.start_time > activity_it.start_time:
                    ok = False
                    break
                if activity.end_time < activity_it.end_time and activity.end_time > activity_it.start_time:
                    ok = False
                    break
                if activity.start_time < activity_it.start_time and activity.end_time > activity_it.end_time:
                    ok = False
                    break
            if ok: 
                activity.user = user
                activity.trip = trip
                activity.save()
                return redirect('trip-detail', pk = trip_pk)
            else:
                messages.add_message(request, messages.ERROR, 'You already have activities planned in this time interval. Please change date/time or modify other activities first!')
    else:
        form = ActivityModelForm()
    return render(request, 'travel/activity_form.html', {'form': form, 'trip': trip})

class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activity

class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    form_class = ActivityModelForm
    template_name = 'travel/activity_form.html'
    success_url = '/dashboard'

    def test_func(self):
        activity = self.get_object()
        trip = activity.trip
        if self.request.user == trip.admin or self.request.user in trip.users.all():
            return True
        else:
            return False
    
class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    success_url = '/'

    def test_func(self):
        activity = self.get_object()
        trip = activity.trip
        if self.request.user == trip.admin or self.request.user in trip.users.all():
            return True
        else:
            return False