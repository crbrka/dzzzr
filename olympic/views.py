from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import *
from .models import *
from .functions import *
import datetime

auth_page = 'auth.html'
logged_page = 'olympic/main.html'
unknown_pattern = '???'  # так показываются неразгаданные поля
now = timezone.now()


def index(request):
    if request.session.get('is_logged', False):
        game = Games.objects.get(id=request.session.get('game_id', 0))  # берем всю информацию по игре
        # codes = " ".join(game.words.split())
        codes = game.words.split(' ')  # из строки в лист
        check_codes = check_code(request,
                                 codes)  # проверка кода, если есть в базе то показываем, если нет то выводим unknown_pattern
        if check_codes.count(
                unknown_pattern) <= game.unnecessary:  # Считаем сколько осталось неразгаданных слов, если меьше или равно нужного кол-во то выводим код
            final_code = game.final_code
        if game.stopdate < now:
            game_stop_date = game.stopdate
        col_count = get_columns_count(codes, game.divider)
        row_count = get_rows_count(codes, game.divider)
        cycles = get_ranges(codes, game.divider)
        form = CodeEnterForm()
        lastcodes = last_codes(request, 10, codes)
        return render(request, logged_page, locals())
    else:
        if request.session.get('pass_error', False):
            error_msg = 'Вы ввели неправильный пароль'
        form = LoginTeamForm(request.POST)
        return render(request, auth_page, locals())


def SendCode(request):  # send new code my team
    form = CodeEnterForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        data = request.POST
        created = datetime.datetime.now()
        ip_addr = request.META['REMOTE_ADDR']
        user_agent = request.META['HTTP_USER_AGENT']
        code = Codes(code=data.get("code"), created=created, game_id=request.session.get('game_id', 1),
                     team_id=request.session.get('team_id', 1), ip_addr=ip_addr, client=user_agent)
        code.save()
    return HttpResponseRedirect('/')


def login(request):  # вход и присвоение сессии всех значений аккаунта и игры
    form = LoginTeamForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        try:
            team = Teams.objects.get(login=request.POST['login'])
            if team.password == request.POST['password']:
                request.session['is_logged'] = True
                request.session['team_id'] = team.id
                request.session['captain'] = team.login
                request.session['team_name'] = team.name
                request.session['game_id'] = team.game_id
            else:
                request.session['pass_error'] = True
        except Teams.DoesNotExist:
            request.session['pass_error'] = True
            pass
    return HttpResponseRedirect('/')


def logout(request):  # Выход из аккаунта
    try:
        session_keys = list(request.session.keys())
        for key in session_keys:
            del request.session[key]
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def last_codes(request, code_count, codes):  # Проверяем последние CODE_COUNT шт. кодов на верность и выводим для информации
    try:
        last = Codes.objects.filter(team_id=request.session.get('team_id', 0),
                                    game_id=request.session.get('game_id', 0), ).order_by('-id')[:code_count]
    except Codes.DoesNotExist:
        pass
    # last_list = list(last)
    for item in list(last):
        if item.code not in codes:
            item.code += ' - НЕВЕРЕН!'
    return last


def check_code(request, game_codes):
    res = []
    try:
        entered_codes = Codes.objects.filter(team_id=request.session.get('team_id', 0),
                                             game_id=request.session.get('game_id', 0), ).values_list('code',
                                                                                                      flat=True).distinct()
    except Codes.DoesNotExist:
        pass
    counter = 0
    for item in game_codes:
        if item in entered_codes:
            res.append(item)
            counter
        else:
            res.append(unknown_pattern)
    return res
