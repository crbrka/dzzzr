from django.contrib import admin
from .models import *

# Register your models here.

class TeamsInline(admin.TabularInline):
    model = Teams
    extra = 0

class GamesInline(admin.TabularInline):
    model = Games
    extra = 0

class GameAdminsAdmin(admin.ModelAdmin):
    list_display = ["id", "login", "name", "created"]
    search_fields = ["login", "name",]
    list_filter = ["login", "name"]
    inlines = [GamesInline]

    class Meta:
        model = GameAdmins

class GamesAdmin(admin.ModelAdmin):
    list_display = ["id", "short_name", "game_admin","created"]
    search_fields = ["short_name","long_name","final_code"]
    inlines = [TeamsInline]

    class Meta:
        model = Games

class TeamsAdmin(admin.ModelAdmin):
    list_display = ["id", "name","login","game_id","created"]
    class Meta:
        model = Teams

admin.site.register(GameAdmins, GameAdminsAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Teams, TeamsAdmin)