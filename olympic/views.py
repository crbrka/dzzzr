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
    game = Games.objects.get(id=request.session.get('game_id', 0))
    codes = game.words.split(' ')
    code_count = tmp = len(codes)
    col_count = 0  #определяем переменные
    row_count = 1
    table = ''
    while tmp > 1:  #считаем кол-во колонок
        tmp /= game.divider
        col_count = col_count + 1
    while True:
        row_count *= game.divider
        if row_count > code_count:
            break
    row_count /= game.divider
    counter = 0
    for item in range(0, col_count, 1):
        table +='<td><div class="flexcontainer">'
        for jtem in range(0, int(row_count), 1):
            counter += 1
            table +='<div class=" flexdiv">'+codes[counter-1]+'</div>'
        row_count /= game.divider
        table +='</div></td>'

    return table







