from django.conf.global_settings import LOGIN_URL
from django.urls import re_path, path
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=LOGIN_URL), name='logout'),
]