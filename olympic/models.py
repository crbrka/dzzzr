from django.db import models


# Create your models here.

class GameAdmins(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_created=True,auto_now=False)
    updated = models.DateTimeField(auto_created=False,auto_now=True)

    def __str__(self):
        return "%s" % (self.login)

    class Meta:
        verbose_name = 'Админ '
        verbose_name_plural = 'Админы '
        db_table = 'dzzzr_gameadmins'


class Games(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_created=True,auto_now=False)
    updated = models.DateTimeField(auto_created=False,auto_now=True)
    stopdate = models.DateTimeField(auto_created=True,auto_now=True)
    game_admin = models.ForeignKey(GameAdmins)
    final_code = models.CharField(max_length=30)
    divider = models.IntegerField(default=3)
    #rows = models.IntegerField(default=4)
    unnecessary = models.IntegerField(default=0)
    words = models.CharField(max_length=5000)


    def __str__(self):
        return "%s" % (self.short_name)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        db_table = 'dzzzr_games'


class Teams(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_created=True, auto_now=False)
    updated = models.DateTimeField(auto_created=False, auto_now=True)
    game = models.ForeignKey(Games)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        db_table = 'dzzzr_teams'


class Codes(models.Model):
    code = models.CharField(max_length=200)
    created = models.DateTimeField(auto_created=True)
    ip_addr = models.CharField(max_length=16,default='127.0.0.2')
    client  = models.CharField(max_length=255)
    game = models.ForeignKey(Games)
    team = models.ForeignKey(Teams)

    def __str__(self):
        return "%s" % (self.code)

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'
        db_table = 'dzzzr_codes'
