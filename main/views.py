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


# Нужно это раскомментировать, запустить один раз, остановить, закомментировать обратно
# cur.execute("BEGIN TRANSACTION; ")
# cur.execute("DELETE FROM main_questions")
# cur.execute("DELETE FROM main_rawquestions")
# cur.execute("COMMIT; ")

questions = ["Обычные обязанности напрягают меня больше чем обычно?",
                 "Я чувствую, что многие на работе открыто конкурируют со мной.",
                 "Могу и накричать. Потом стыдно. Раньше так не было.",
                 "Я боюсь все испортить в работе и всех подвести.",
                 "Выполняю работу как робот, иногда не могу остановиться.",
                 "Меня напрягает, если надо выполнять работу вместе с кем-то.",
                 "Меня не радует проделанная работа.",
                 "В последнее время, мне часто приходится оправдываться за свою неадекватную реакцию.",
                 "Я чувствую себя колхозной лошадью, которая работает больше всех и никогда не станет председателем.",
                 "Я чувствую, что отвечаю на вопросы случайным образом.",
                 "В последнее время я не очень охотно присоединяюсь к эмоциям других.",
                 "Мне стало проще сделать все самостоятельно, чем просить кого-то.",
                 "У меня такое чувство, что мой организм предательски активно протестует против моего режима работы и старается выбить меня из колеи.",
                 "Меня чаще стало тревожить, правильно ли я выполняю работу.",
                 "У меня нет сил ни с кем общаться на работе, делиться своими новостями, печалями и радостями.",
                 "Я постоянно чувствую себя уставшим.",
                 "Я становлюсь нечувствительным к проблемам и страданиям других.",
                 "Я буквально заставляю себя каждый день идти на работу.",
                 "Я все принимаю близко к сердцу."]

answers = ["Совершенно неверно",
               "Скорее неверно",
               "Точно не могу сказать",
               "Скорее верно",
               "Совершенно верно"]


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
        month = datetime.now().month
        year = datetime.now().year

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
            cur.execute("BEGIN TRANSACTION; ")
            cur.execute(
                "INSERT INTO main_rawquestions (id, employee_login, question, answer, month, year) VALUES (NULL, '%s', '%d', '%d', '%d', '%d')" % (username, i, int(arr[i]), int(month), int(year)))
            cur.execute("COMMIT;")

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
        cur.execute("BEGIN TRANSACTION; ")
        cur.execute(
            "INSERT INTO main_questions (id, employee_login, condition, month, year) VALUES (NULL, '%s', '%s', '%d', '%d');" % (username, result, int(month), int(year)))
        cur.execute("COMMIT;")
        return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def master(request):
    return render(request, 'master.html')


def slave(request):
    if request.method == 'POST':
        print('Goliath online')


def make_results(db_response):
    res = {}
    for row in db_response:
        user = row[1]
        if user not in res:
            res[user] = []
        res[user].append([row[2], row[3], row[4], row[5]])
    return res


def results(request):
    all_users = User.objects.filter(groups__name='Slaves').values()
    month = datetime.now().month
    year = datetime.now().year

    raw_results = {}
    processed_results = {}

    for user_info in all_users:
        username = user_info['username']
        first_name = user_info['first_name']
        last_name = user_info['last_name']
        full_name = first_name + " " + last_name

        raw_db = cur.execute(
            "SELECT question, answer FROM (SELECT * FROM main_rawquestions WHERE employee_login='%s' AND month='%d' AND year='%d');" % (username, int(month), int(year)))
        raw_for_user = raw_db.fetchall()
        raw_results[full_name] = []
        for info in raw_for_user:
            current_raw = {'Question': questions[info[0]], 'Answer': answers[info[1]]}
            raw_results[full_name].append(current_raw)

        processed_for_user_db = cur.execute(
            "SELECT condition FROM (SELECT * FROM main_questions WHERE employee_login='%s' AND month='%d' AND year='%d');" % (username, int(month), int(year)))
        processed_for_user = processed_for_user_db.fetchall()
        processed_results[full_name] = []
        for info in processed_for_user:
            current_processed = {'TestResult': info[0]}
            processed_results[full_name].append(current_processed)

    res = {"Raw_results": raw_results, "Processed_results" : processed_results}
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
