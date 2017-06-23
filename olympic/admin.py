from django.contrib import admin
from .models import *


# Register your models here.

class TeamsInline(admin.TabularInline):
    model = Teams
    extra = 0

class GamesInline(admin.TabularInline):
    model = Games
    extra = 0

class CodesInline(admin.TabularInline):
    model = Codes
    extra = 0
    readonly_fields = ["code","created","ip_addr","game","team","client"]


class GamesAdmin(admin.ModelAdmin):
    list_display = ["id", "short_name", "game_admin", "created", "words"]
    search_fields = ["short_name","long_name","final_code"]
    inlines = [TeamsInline,CodesInline]

    class Meta:
        model = Games

class TeamsAdmin(admin.ModelAdmin):
    list_display = ["id", "name","login","game_id","created"]
    inlines = [CodesInline]

    class Meta:
        model = Teams

class CodesAdmin(admin.ModelAdmin):
    list_display = ["id","code","team_id","game_id","ip_addr","created"]
    class Meta:
        model = Codes

admin.site.register(Games, GamesAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Codes, CodesAdmin)