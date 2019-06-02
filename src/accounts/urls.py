from django.urls import path
from .views import base_view, logged_out_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page="/accounts/logged_out_success"), name="logout"),
    path('logged_out_success/', logged_out_view),
    path('', base_view),
]
