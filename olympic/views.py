from django.shortcuts import render
#from django.contrib import sessions
from . import urls
from .forms import *
from .models import *


# Create your views here.


def index(request):
    is_user = request.session.get('is_valid')
    if not is_user == 'True':
        print(request.POST)
        print('HELLOE')
        u = Teams.objects.get(login=request.POST.get('username'))
        if u.password == request.POST['password']:
            request.session['member_id'] = m.id
            request.session['is_valid'] = True;
        return render(request, 'olympic/auth.html', locals())
    else:
        print(request.session.get('is_valid'))
        print('BBB')
        return render(request, 'olympic/main.html', locals())

