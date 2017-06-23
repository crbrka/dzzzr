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

