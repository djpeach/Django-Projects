from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Your account has been created, go ahead an log in!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(req, 'users/register.html', {'form': form})


@login_required
def profile(req):
    if req.method == 'POST':
        user_update_form = UserUpdateForm(req.POST, instance=req.user)
        profile_update_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(req, f'Your account has been updated!')
            return redirect('users_profile')
    else:
        user_update_form = UserUpdateForm(instance=req.user)
        profile_update_form = ProfileUpdateForm(instance=req.user.profile)
    
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    
    return render(req, 'users/profile.html', context)
