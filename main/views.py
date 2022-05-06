from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime

import sqlite3

con = sqlite3.connect('users.db', check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users 
               (username, password, email, admin)''')
cur.execute('''CREATE TABLE IF NOT EXISTS raw_results(username, question, answer, month, year)''')
cur.execute('''CREATE TABLE IF NOT EXISTS processed_results(username, attribute, value, month, year)''')

def home(request):
    return render(request, 'home.html')

def master(request):
    return render(request, 'master.html')

def slave(request):
    return render(request, 'slave.html')

def results(request):
    all_users = User.objects.filter(groups__name='Slaves').values()
    month = datetime.now().month
    year = datetime.now().year
    raw_results = cur.execute("SELECT * FROM raw_results WHERE month = '%s' AND year = '%s'" % (month, year))  # Сырые
    # результаты за месяц
    processed_results = cur.execute(
        "SELECT * FROM processed_results WHERE month = '%s' AND year = '%s'" % (month, year))  # Обработанные
    # результаты за месяц
    res = {"Name": all_users}
    return render(request, "results.html", context=res)

def slave_profile(request):
    return render(request, 'profile.html')

def master_profile(request):
    return render(request, "profile-master.html")

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
                else:
                    login(request, user)
                return render(request, 'home.html')
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

def logout(request):
    django_logout(request)
    return render(request, 'logout.html')

class ProfilePage(TemplateView):
    template_name = "profile.html"

class TestPage(TemplateView):
    template_name = "slave.html"

def get_slaves():
    users = get_user_model().objects.all()
    result = []
    for user in users:
        if user.groups.all()[0].name == "Slaves":
            result.append(user)
    return result
