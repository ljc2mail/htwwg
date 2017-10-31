from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .admin import UserCreationForm, Friend
from .forms import EditProfileForm
from .models import MyUser

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('user:profile')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form})


def profile(request):
    #user = request.user
    others = MyUser.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    #print(friends_users)
    args = {'user': request.user, 'friends': friends, 'others': others}
    return render(request, 'authentication/profile.html', args)

def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #picture = form.cleaned_data.get('picture.name')
            #print(picture)
            form.save()
            user = authenticate(email=email, password=raw_password)
            return redirect('user:profile')
    else:
         form =  EditProfileForm(instance=request.user)

    return render(request, 'authentication/edit_profile.html', {'form': form})


def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('htwwg:sighting_list')
    else:
         form =  PasswordChangeForm(user=request.user)

    return render(request, 'authentication/passwordchange.html', {'form': form})

def changefriend(request, Op, pk):
    friend=MyUser.objects.get(pk=pk)
    if Op=='add':
        Friend.Make_A_Friend(request.user,friend)
    elif Op=='remove':
        Friend.Lose_A_Friend(request.user,friend)
    return redirect('user:profile')