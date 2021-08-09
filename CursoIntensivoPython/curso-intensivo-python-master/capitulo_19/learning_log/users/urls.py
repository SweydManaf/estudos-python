"""Define padrões de URL para users."""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'users'
urlpatterns = [
    # Página de login.
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),

    # Página de logout.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Página de cadastro.
    path('register/', views.register, name='register'),
]
