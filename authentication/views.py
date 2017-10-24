from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .admin import UserCreationForm
from .forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

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
	args = {'user': request.user}
	return render(request, 'authentication/profile.html', args)


def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
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