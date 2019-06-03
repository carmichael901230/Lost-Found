from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm #,UserProfileForm
from django.contrib.auth import authenticate, login


def base_view(request):
    return render(request, 'base.html')

def logged_out_view(request):
    return render(request, 'accounts/logged_out.html')

def register_view(request):
    if request.method == 'POST':
        register_form  = UserRegisterForm(request.POST)
        # profile_form = UserProfileForm(request.POST)
        if register_form.is_valid():# and profile_form.is_valid():
            user = register_form.save()
            # profile_form.save(commit=False)
            # profile_form.user = user
            # profile_form.save(commit=True)

            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:base')
    else:
        register_form = UserRegisterForm()
        # profile_form = UserProfileForm()
    context = {
        'register_form':register_form,
        # 'profile_form':profile_form    
    }
    return render(request, 'accounts/register.html', context)
