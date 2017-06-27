from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from olympic.models import *
from django.utils import timezone
import datetime


auth_page = 'auth.html'
adminpage = 'adminpanel/gamepanel.html'
firstgame = 'adminpanel/firstgame.html'


def adminpanel(request):
    if request.session.get('admin_is_logged', False):
        if not len(request.session.get('admin_games')) == 0:
            active_game = list(Games.objects.filter(id=request.session['active_game'][0]).values_list())
            return render(request, adminpage, locals())
        else:
            return render(request, firstgame, locals())
    else:
        if request.session.get('pass_error', False):
            error_msg = 'Вы ввели неправильный пароль'
        form = LoginAdminForm(request.POST)
        return render(request, auth_page, locals())




def hello(request):
    form = LoginAdminForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        try:
            gmadmin = GameAdmins.objects.get(login=request.POST['login'])
            print(request.POST)
            if gmadmin.password == request.POST['password']:
                request.session['admin_is_logged'] = True
                request.session['admin_id'] = gmadmin.id
                request.session['admin_name'] = gmadmin.name
                request.session['admin_games'] = list(Games.objects.filter(game_admin=gmadmin.id).values_list('id','long_name'))
                request.session['active_game'] = request.session.get('admin_games')[-1] # выбираем последюю созданую игру, как игра по умолчанию
            else:
                request.session['pass_error'] = True
        except GameAdmins.DoesNotExist:
            request.session['pass_error'] = True
            pass
    return HttpResponseRedirect('/admin')


def goodbye(request):
    try:
        session_keys = list(request.session.keys())
        for key in session_keys:
            del request.session[key]
    except KeyError:
        pass
    return HttpResponseRedirect('/admin')