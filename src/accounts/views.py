from django.shortcuts import render, HttpResponse


def base_view(request):
    return render(request, 'base.html')

def logged_out_view(request):
    return render(request, 'accounts/logged_out.html')
