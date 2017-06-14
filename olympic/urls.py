from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sendcode$', views.SendCode, name='sendcode'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$',views.logout, name='logout'),


]