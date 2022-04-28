from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/profile/', views.slave_profile(), name="profile"),
    path('accounts/profile-master/', views.master_profile(), name="profile-master"),
    path(r'^accounts/register/$', views.RegisterView.as_view(), name="register"),
    path('accounts/slave/', views.TestPage.as_view(), name="slave"),
    path(r'^accounts/register_pro/$', views.RegisterView.as_view(), name="register_pro"),
    path('', views.home),
    path('master', views.master),
]
