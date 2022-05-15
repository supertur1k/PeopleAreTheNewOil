from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/logout/', views.logout, name="logout"),
    path('accounts/profile/', views.slave_profile, name="profile"),
    path('accounts/boss/', views.master_profile, name="profile-master"),
    path('accounts/slave/', views.MyView.as_view(), name="slave"),
    path('accounts/results', views.results, name="results"),
    path('', views.home),
    path('master', views.master),
]
