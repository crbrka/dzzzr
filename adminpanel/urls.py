from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.adminpanel, name='adminpanel'),
    url(r'^login$', views.hello, name='hello'),
    url(r'^logout$', views.goodbye, name='goodbye'),
   # url(r'^newgame$', views.newgame, name='newgame'),
   # url(r'^game$', views.game, name='game'),

]