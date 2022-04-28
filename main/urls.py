from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/profile/', views.ProfilePage.as_view(), name="profile"),
    path(r'^accounts/register/$', views.RegisterView.as_view(), name="register"),
    path(r'^accounts/register_pro/$', views.RegisterView.as_view(), name="register_pro"),
    path('', views.home),
    path('login', views.login),
    path('master', views.master),
    path('slave', views.slave)
]
