from django.urls import path
from . import views
from .views import TripCreateView, TripDetailView, TripUpdateView, TripDeleteView, ActivityDetailView, ActivityDeleteView, ActivityUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('trip/new', TripCreateView.as_view(), name='create-trip'),
    path('trip/<int:pk>', TripDetailView.as_view(), name='trip-detail'),
    path('trip/<int:pk>/edit', TripUpdateView.as_view(), name='update-trip-details'),
    path('trip/<int:pk>/delete', TripDeleteView.as_view(), name='delete-trip'),
    path('trip/<int:trip_pk>/add-activity', views.add_activity, name='add-activity'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('trip/activity/<int:pk>', ActivityDetailView.as_view(), name='activity-detail'),
    path('trip/activity/<int:pk>/edit', ActivityUpdateView.as_view(), name='activity-update'),
    path('trip/activity/<int:pk>/delete', ActivityDeleteView.as_view(), name='delete-activity'),
    path('trip/<int:trip_pk>/users', views.trip_users, name='manage-trip-users'),
]