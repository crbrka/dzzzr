from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
import datetime

auth_page = 'olympic/auth.html'
logged_page = 'olympic/main.html'


def get_columns_count(codes,divider):  # считаем кол-во колонок
    codes_count = len(codes)
    delitel = 1
    counter = 1
    while not codes_count < delitel*divider:
        delitel *= divider
        counter += 1
    return counter


def get_ranges(codes,divider):  # считаем кол-во диапазонов
    codes_count = len(codes)
    delitel = counter = 1
    ranges = [range(1)]
    while not codes_count < delitel*divider:
        delitel *= divider
        counter += 1
        ranges.append(range(delitel))
    return ranges


def get_rows_count(codes, divider):
    codes_count = len(codes)
    row_count = 1
    while True:
        row_count *= divider
        if row_count > codes_count:
            break
    row_count /= divider
    return int(row_count)

def index(request):
    if request.session.get('is_logged', False):
        game = Games.objects.get(id=request.session.get('game_id', 0))  # берем всю информацию по игре
        codes = game.words.split(' ')  # из строки в лист
        col_count = get_columns_count(codes, game.divider)
        row_count = get_rows_count(codes, game.divider)
        cycles = get_ranges(codes, game.divider)
        form = CodeEnterForm()
        last_codes(request,10)
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
        code = Codes(code=data.get("code"), created=created, game_id=request.session.get('game_id', 1), team_id=request.session.get('team_id', 1), ip_addr=ip_addr, client=user_agent)
        code.save()
    return HttpResponseRedirect('/')


def login(request):
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


def logout(request):
    try:
        session_keys = list(request.session.keys())
        for key in session_keys:
            del request.session[key]
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def last_codes(request, code_count):
    try:
        last = Codes.objects.get(team_id=request.session.get('team_id',0),game_id=request.session.get('game_id',0))
    except Codes.DoesNotExist:
            pass
    print(last[1])

