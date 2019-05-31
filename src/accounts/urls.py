from django.urls import path
from .views import base_view
from django.contrib.auth.views import LoginView

# app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('', base_view),
]
