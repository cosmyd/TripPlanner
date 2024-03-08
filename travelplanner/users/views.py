from django.shortcuts import render, redirect
from .forms import UserRegisterForm, FriendRequestForm
from django.contrib.auth.decorators import login_required
from .models import FriendshipList


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def friends_list(request):
    user = request.user
    friends_list = FriendshipList.objects.filter(owner=user)
    
    context = {
        'friends_list': friends_list
    }
    return render(request, 'users/friends_list.html', context)

@login_required
def send_friend_request(request):
    user = request.user
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.from_user = user
            friend_request = form.save()
    else:
        form = FriendRequestForm()
    return render(request, 'users/send_friend_request.html',{'form': form})        




