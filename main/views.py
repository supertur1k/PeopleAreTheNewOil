from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'home.html')

def master(request):
    return render(request, 'master.html')

def slave(request):
    return render(request, 'slave.html')

def slave_profile(request):
    return render(request, 'profile.html')

def master_profile(request):
    all_users = User.objects.filter(groups__name='Slaves').values()
    res = {"Name" : all_users}
    return render(request, "profile-master.html", context=res)

class LoginView(TemplateView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.all()[0].name == "Master":
                    login(request, user)
                    return redirect(reverse("profile-master"))
                else:
                    login(request, user)
                    return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class LogoutView(TemplateView):
    template_name = "logout.html"

class ProfilePage(TemplateView):
    template_name = "profile.html"

class TestPage(TemplateView):
    template_name = "slave.html"

class RegisterView(TemplateView):
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)


def get_slaves():
    users = get_user_model().objects.all()
    result = []
    for elem in users:
        if user.groups.all()[0].name == "Slaves":
            result.append(elem)
    return result
