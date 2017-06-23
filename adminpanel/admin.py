from django.contrib import admin
from .models import *
from olympic import models

# Register your models here.
class GameAdminsAdmin(admin.ModelAdmin):
    list_display = ["id", "login", "name", "created"]
    search_fields = ["login", "name",]
    list_filter = ["login", "name"]
  #  inlines = ['olympic.GamesInline']

    class Meta:
        model = GameAdmins

admin.site.register(GameAdmins, GameAdminsAdmin)
