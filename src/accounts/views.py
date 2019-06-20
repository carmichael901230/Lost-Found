from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm, UserEditForm
from profiles.forms import UserProfileForm, ProfileEditForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from profiles.models import Profile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def logged_out_view(request):
    return render(request, 'accounts/logged_out.html')

def register_view(request):
    if request.method == 'POST':
        register_form  = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save( )

            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
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

@login_required
def profile_view(request):
    context = {
        'user': request.user,
        'profile': Profile.objects.get(user__id=request.user.pk)
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_edit_view(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=Profile.objects.get(user__id=request.user.pk))
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('accounts:profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=Profile.objects.get(user__id=request.user.pk))
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'profile':Profile.objects.get(user__id=request.user.pk)
        }
        return render(request, "accounts/profile_edit.html", context)

@login_required
def change_pw_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, "accounts/change_password.html", context)
