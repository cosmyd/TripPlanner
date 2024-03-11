from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, FriendRequestForm
from django.contrib.auth.decorators import login_required
from .models import FriendshipList, FriendRequest
from django.contrib import messages


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
    present_friends = FriendshipList.objects.get(owner = user).friends.all()
    print(present_friends)
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            if friend_request.to_user in present_friends:
                print('hereeee')
                messages.add_message(request, messages.ERROR, 'You are already friends with this person')
            else:
                friend_request.from_user = user
                friend_request = form.save()
    else:
        form = FriendRequestForm()
    return render(request, 'users/send_friend_request.html',{'form': form})        

@login_required
def friend_requests(request):
    user = request.user
    friend_requests = FriendRequest.objects.filter(to_user = user)
    context = {
        'friend_requests': friend_requests
    }
    return render(request, 'users/friend_requests.html', context)    

@login_required
def friend_request_accept(request, fr_pk):
    friend_request = get_object_or_404(FriendRequest, pk=fr_pk)
    from_user = friend_request.from_user
    to_user = friend_request.to_user
    if to_user == request.user:
        FriendshipList.objects.get(owner = request.user).friends.add(from_user)
        FriendshipList.objects.get(owner = from_user).friends.add(request.user)
        friend_request.delete()
    return redirect('friend-requests')


    



