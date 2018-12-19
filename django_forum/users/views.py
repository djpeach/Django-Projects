from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

def register(req):
    if(req.method == 'POST'):
        form = forms.UserRegistrationForm(req.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form = forms.UserRegistrationForm()
    return render(req, 'users/register.html', {'form': form})
