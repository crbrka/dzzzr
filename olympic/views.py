from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import urls
from .forms import *
from .models import *
import datetime

auth_page = 'olympic/auth.html'
logged_page = 'olympic/main.html'



def index(request):
    if request.session.get('is_logged', False):
        game_info = Games.objects.get(id=request.session.get('game_id',1))
        answer_table=draw_table(request)
        form = CodeEnterForm()
        return render(request, logged_page, locals())
    else:
        if request.session.get('pass_error', False):
            error_msg = 'Вы ввели неправильный пароль'
        form = LoginTeamForm(request.POST)
        return render(request, auth_page, locals())

def SendCode(request): # send new code my team
    form = CodeEnterForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        data = request.POST
        created = datetime.datetime.now()
        ip_addr = request.META['REMOTE_ADDR']
        user_agent = request.META['HTTP_USER_AGENT']
        code = Codes(code=data.get("code"),created=created,game_id=request.session.get('game_id',1),team_id=request.session.get('team_id',1),ip_addr=ip_addr,client=user_agent)
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

def draw_table(request):
    game_info = Games.objects.get(id=request.session.get('game_id', 1))
    counter = len(game_info.words.split(' ')) # определяем количество кодов
    col_count=0
    table='hello world'
    while counter > 1: #смотрим сколько будет колонок, учитывая известный делитель
        counter = counter / game_info.divider
        col_count = col_count+1
    for i in range(1, game_info.rows, ):
        table = table+'<tr>'
        for j in range(1, col_count, 1):
            table = table+'<td>-</td>'
        table = table+'</tr>'
    return table



