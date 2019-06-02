from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

def base_view(request):
    context = {'user': request.user}
    return render(request, 'base.html', context)

def loggedout_view(request):
    return render(request, 'accounts/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:base')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
