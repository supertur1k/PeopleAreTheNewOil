from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime

import sqlite3

con = sqlite3.connect('db.sqlite3', check_same_thread=False)
cur = con.cursor()


class MyView(TemplateView):
    template_name = "slave.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'slave.html')

    def post(self, request):
        arr = request.POST.get('19')
        username = request.POST.get('username')

        completely_wrong = 0
        probably_wrong = 0
        can_not_say = 0
        probably_correct = 0
        absolutely_correct = 0

        for i in range(19):
            if arr[i] == "0":
                completely_wrong = completely_wrong + 1
            if arr[i] == "1":
                probably_wrong = probably_wrong + 1
            if arr[i] == "2":
                can_not_say = can_not_say + 1
            if arr[i] == "3":
                probably_correct = probably_correct + 1
            if arr[i] == "4":
                absolutely_correct = absolutely_correct + 1

        result = ""

        if completely_wrong > 14 or probably_wrong > 18:
            result = "Сотрудник абсолютно здоров психолигчески и готов к продуктивной работе!"

        elif absolutely_correct > 14 or probably_correct > 18:
            result = "Сотрудник сталкивается с большими трудностями в работе. Система выявида у сотрудника " \
                     "признаки эмоцианального выгорания. Настоятельно рекомендуем работодателю провести беседу. " \
                     "Возможные сценарии: смена коллектива, отпуск, изменение условий работы. "

        elif can_not_say > 14:
            result = "Система не может однозначно выявить симптомы эмоционального выгорания у сотрудника. " \
                     "Рекомендуется консультация специалиста"

        elif 14 > completely_wrong > 8 or 18 > probably_wrong > 12:
            result = "Сотрудник достаточно хорошо справляется с работой, но к увеличению нагрузок с сохранением " \
                     "текущих условий труда не готов."

        elif 14 > absolutely_correct > 8 or 18 > probably_correct > 12:
            result = "Ярко выраженных симптомов эмоционального выгорания не выявлено, однако, работодателю " \
                     "рекомендуется обратить внимания на условия труда своего сотрудника. В случае сохранения " \
                     "текущих условий без предоставления отпуска, в ближайшем будущем есть риск просадки в" \
                     " продуктивности."

        else:
            result = "Результаты опроса не позволяют системе однозначно понять психологическое состояние сотрудника. " \
                     "Рекомендуется консультация со специалистом."

        print("Сотрудник: ", username, "\nРезультат: ", result)
        return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def master(request):
    return render(request, 'master.html')


def slave(request):
    if request.method == 'POST':
        print('Goliath online')


def results(request):
    all_users = User.objects.filter(groups__name='Slaves').values()
    month = datetime.now().month
    year = datetime.now().year
    processed_results = cur.execute(
        "SELECT * FROM main_rawquestions")
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
