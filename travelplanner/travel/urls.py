from django.urls import path
from . import views
from .views import TripCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('trip/new', TripCreateView.as_view(), name='create-trip'),
    
]