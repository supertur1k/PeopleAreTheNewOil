let testQuestion = "Я чувствую, что отвечаю на вопросы случайным образом."
var clientAns = []
document.addEventListener('DOMContentLoaded', function(){
    let questions = ["Обычные обязанности напрягают меня больше чем обычно?",
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
    q_with_a = []
    for (var i = 0; i < 19; ++i) {
        q_with_a.push([questions[i], answers[i]])
    }
    q_with_a = mix(q_with_a);
    document.getElementById('q_1').innerHTML = q_with_a[0][0];
    document.getElementById('q_2').innerHTML = q_with_a[1][0];
    document.getElementById('q_3').innerHTML = q_with_a[2][0];
    document.getElementById('q_4').innerHTML = q_with_a[3][0];
    document.getElementById('q_5').innerHTML = q_with_a[4][0];
    document.getElementById('q_6').innerHTML = q_with_a[5][0];
    document.getElementById('q_7').innerHTML = q_with_a[6][0];
    document.getElementById('q_8').innerHTML = q_with_a[7][0];
    document.getElementById('q_9').innerHTML = q_with_a[8][0];
    document.getElementById('q_10').innerHTML = q_with_a[9][0];
    document.getElementById('q_11').innerHTML = q_with_a[10][0];
    document.getElementById('q_12').innerHTML = q_with_a[11][0];
    document.getElementById('q_13').innerHTML = q_with_a[12][0];
    document.getElementById('q_14').innerHTML = q_with_a[13][0];
    document.getElementById('q_15').innerHTML = q_with_a[14][0];
    document.getElementById('q_16').innerHTML = q_with_a[15][0];
    document.getElementById('q_17').innerHTML = q_with_a[16][0];
    document.getElementById('q_18').innerHTML = q_with_a[17][0];
    document.getElementById('q_19').innerHTML = q_with_a[18][0];
});

function mix(q) {
    for (var i = q.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = q[i];
        q[i] = q[j];
        q[j] = tmp;
    }
    return q;
}

function AfterClick(question, answer) {
    clientAns[question - 1] = answer;
}

function end() {
    document.getElementById('q19').style.display = "none";
    document.getElementById('kn_sl').style.display = "none";
    document.getElementById('kn_end').style.display = "none";
    document.getElementById('kn_com').style.display = "block";
    document.getElementById('end').style.display = "block";
}

function comment() {
    document.getElementById('kn_com').style.display = "none";
    document.getElementById('comment').style.display = "block";
}

function next_question() {
    if(document.getElementById('q18').style.display === "block"){
        document.getElementById('q18').style.display = "none";
        document.getElementById('q19').style.display = "block";
        document.getElementById('kn_sl').style.display = "none";
        document.getElementById('kn_end').style.display = "block";
    }
    if(document.getElementById('q17').style.display === "block"){
        document.getElementById('q17').style.display = "none";
        document.getElementById('q18').style.display = "block";
    }
    if(document.getElementById('q16').style.display === "block"){
        document.getElementById('q16').style.display = "none";
        document.getElementById('q17').style.display = "block";
    }
    if(document.getElementById('q15').style.display === "block"){
        document.getElementById('q15').style.display = "none";
        document.getElementById('q16').style.display = "block";
    }
    if(document.getElementById('q14').style.display === "block"){
        document.getElementById('q14').style.display = "none";
        document.getElementById('q15').style.display = "block";
    }
    if(document.getElementById('q13').style.display === "block"){
        document.getElementById('q13').style.display = "none";
        document.getElementById('q14').style.display = "block";
    }
    if(document.getElementById('q12').style.display === "block"){
        document.getElementById('q12').style.display = "none";
        document.getElementById('q13').style.display = "block";
    }
    if(document.getElementById('q11').style.display === "block"){
        document.getElementById('q11').style.display = "none";
        document.getElementById('q12').style.display = "block";
    }
    if(document.getElementById('q10').style.display === "block"){
        document.getElementById('q10').style.display = "none";
        document.getElementById('q11').style.display = "block";
    }
    if(document.getElementById('q9').style.display === "block"){
        document.getElementById('q9').style.display = "none";
        document.getElementById('q10').style.display = "block";
    }
    if(document.getElementById('q8').style.display === "block"){
        document.getElementById('q8').style.display = "none";
        document.getElementById('q9').style.display = "block";
    }
    if(document.getElementById('q7').style.display === "block"){
        document.getElementById('q7').style.display = "none";
        document.getElementById('q8').style.display = "block";
    }
    if(document.getElementById('q6').style.display === "block"){
        document.getElementById('q6').style.display = "none";
        document.getElementById('q7').style.display = "block";
    }
    if(document.getElementById('q5').style.display === "block"){
        document.getElementById('q5').style.display = "none";
        document.getElementById('q6').style.display = "block";
    }
    if(document.getElementById('q4').style.display === "block"){
        document.getElementById('q4').style.display = "none";
        document.getElementById('q5').style.display = "block";
    }
    if(document.getElementById('q3').style.display === "block"){
        document.getElementById('q3').style.display = "none";
        document.getElementById('q4').style.display = "block";
    }
    if(document.getElementById('q2').style.display === "block"){
        document.getElementById('q2').style.display = "none";
        document.getElementById('q3').style.display = "block";
    }
    if(document.getElementById('q1').style.display === "block"){
        document.getElementById('q1').style.display = "none";
        document.getElementById('q2').style.display = "block";
    }
}