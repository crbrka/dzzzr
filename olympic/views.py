from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import urls
from .forms import *
from .models import *

auth_page = 'olympic/auth.html'
logged_page = 'olympic/main.html'

def index(request):

    if request.session.get('is_logged', False):
        return render(request, logged_page, locals())
    else:
        if request.session.get('404', False):
            error_msg = 'Вы ввели неправильный пароль'
        form = LoginTeamForm(request.POST)
        return render(request, auth_page, locals())



def login(request):
    form = LoginTeamForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        try:
            team = Teams.objects.get(login=request.POST['login'])
            if team.password == request.POST['password']:
                request.session['is_logged'] = True
                request.session['team_id'] = team.id
                request.session['team_name'] = team.name
                request.session['game_id'] = team.game_id
            else:
                request.session['404'] = True
        except Teams.DoesNotExist:
            request.session['404'] = True
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



