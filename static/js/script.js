var is_ans = []
var ans = ""
var questions = ["Обычные обязанности напрягают меня больше чем обычно?",
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
let answers = ["Совершенно неверно",
               "Скорее неверно",
               "Точно не могу сказать",
               "Скорее верно",
               "Совершенно верно"]

document.addEventListener('DOMContentLoaded', function() {
    for (var i = 0; i < 19; ++i) {
        is_ans[i] = false;
    }
});


function AfterClick(question, answer) {
    if (is_ans[question - 1] === true) {
        ans = ans.slice(0, -1);
    }
    ans += answer;
    is_ans[question - 1] = true;
}

function next_question() {
    if(document.getElementById('q18').style.display === "block") {
        if (!is_ans[17]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q18').style.display = "none";
            document.getElementById('q19').style.display = "block";
            document.getElementById('kn_sl').style.display = "none";
            document.getElementById('radio-19-1').value = ans + '0';
            document.getElementById('radio-19-2').value = ans + '1';
            document.getElementById('radio-19-3').value = ans + '2';
            document.getElementById('radio-19-4').value = ans + '3';
            document.getElementById('radio-19-5').value = ans + '4';
        }
    }
    if(document.getElementById('q17').style.display === "block") {
        if (!is_ans[16]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q17').style.display = "none";
            document.getElementById('q18').style.display = "block";
        }
    }
    if(document.getElementById('q16').style.display === "block") {
        if (!is_ans[15]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q16').style.display = "none";
            document.getElementById('q17').style.display = "block";
        }
    }
    if(document.getElementById('q15').style.display === "block") {
        if (!is_ans[14]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q15').style.display = "none";
            document.getElementById('q16').style.display = "block";
        }
    }
    if(document.getElementById('q14').style.display === "block") {
        if (!is_ans[13]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q14').style.display = "none";
            document.getElementById('q15').style.display = "block";
        }
    }
    if(document.getElementById('q13').style.display === "block") {
        if (!is_ans[12]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q13').style.display = "none";
            document.getElementById('q14').style.display = "block";
        }
    }
    if(document.getElementById('q12').style.display === "block") {
        if (!is_ans[11]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q12').style.display = "none";
            document.getElementById('q13').style.display = "block";
        }
    }
    if(document.getElementById('q11').style.display === "block") {
        if (!is_ans[10]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q11').style.display = "none";
            document.getElementById('q12').style.display = "block";
        }
    }
    if(document.getElementById('q10').style.display === "block") {
        if (!is_ans[9]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q10').style.display = "none";
            document.getElementById('q11').style.display = "block";
        }
    }
    if(document.getElementById('q9').style.display === "block") {
        if (!is_ans[8]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q9').style.display = "none";
            document.getElementById('q10').style.display = "block";
        }
    }
    if(document.getElementById('q8').style.display === "block") {
        if (!is_ans[7]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q8').style.display = "none";
            document.getElementById('q9').style.display = "block";
        }
    }
    if(document.getElementById('q7').style.display === "block") {
        if (!is_ans[6]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q7').style.display = "none";
            document.getElementById('q8').style.display = "block";
        }
    }
    if(document.getElementById('q6').style.display === "block") {
        if (!is_ans[5]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q6').style.display = "none";
            document.getElementById('q7').style.display = "block";
        }
    }
    if(document.getElementById('q5').style.display === "block") {
        if (!is_ans[4]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q5').style.display = "none";
            document.getElementById('q6').style.display = "block";
        }
    }
    if(document.getElementById('q4').style.display === "block") {
        if (!is_ans[3]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q4').style.display = "none";
            document.getElementById('q5').style.display = "block";
        }
    }
    if(document.getElementById('q3').style.display === "block") {
        if (!is_ans[2]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q3').style.display = "none";
            document.getElementById('q4').style.display = "block";
        }
    }
    if(document.getElementById('q2').style.display === "block") {
        if (!is_ans[1]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q2').style.display = "none";
            document.getElementById('q3').style.display = "block";
        }
    }
    if(document.getElementById('q1').style.display === "block") {
        if (!is_ans[0]) {
            alert("Вы не ответили на данный вопрос!");
        } else {
            document.getElementById('q1').style.display = "none";
            document.getElementById('q2').style.display = "block";
        }
    }
}