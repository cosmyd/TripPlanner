from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', next_page="home"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', next_page="logout"), name='logout'),
    path('friends/', views.friends_list, name='friends-list' ),
    path('friends/add', views.send_friend_request, name='send-friend-request')
]
