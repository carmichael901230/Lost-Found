from django.shortcuts import render, HttpResponse

# Create your views here.
# def login_view(request):
#     return render(request, 'accounts/login.html')

def base_view(request):
    return render(request, 'base.html')