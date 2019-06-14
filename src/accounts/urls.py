from django.urls import path
from .views import logged_out_view, register_view, profile_view, profile_edit_view, change_pw_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page="/accounts/logged_out_success"), name="logout"),
    path('logged_out_success/', logged_out_view, name='logged_out'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('change_password/', change_pw_view, name='change_password'),
]
