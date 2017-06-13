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
    game_admin = models.ForeignKey(GameAdmins)
    final_code = models.CharField(max_length=30)
    codes = models.TextField

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
        return "%s - %s" % (self.game_id, self.name)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        db_table = 'dzzzr_teams'


