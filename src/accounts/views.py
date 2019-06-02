from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from profiles.forms import UserProfileForm
from .forms import UserRegisterForm

def base_view(request):
    context = {'user': request.user}
    return render(request, 'base.html', context)

def loggedout_view(request):
    return render(request, 'accounts/logout.html')

def register_view(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST or None)
        register_form  = UserRegisterForm(request.POST or None)
        if register_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save(commit=True)

            username = user.cleaned_data.get('username')
            raw_password = user.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:base')
    else:
        register_form = UserRegisterForm()
        profile_form = UserProfileForm()
        context = {
            'register_form':register_form,
            'profile_form':profile_form    
        }
    return render(request, 'accounts/register.html', context)
