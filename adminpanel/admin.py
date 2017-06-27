from django.contrib import admin
from .models import *
from olympic.models import Games

# Register your models here.

class GameAdminsAdmin(admin.ModelAdmin):
    list_display = ["id", "login", "name", "created"]
    search_fields = ["login", "name",]
    list_filter = ["login", "name"]
   # inlines = [GamesInline]

    class Meta:
        model = GameAdmins

admin.site.register(GameAdmins, GameAdminsAdmin)
