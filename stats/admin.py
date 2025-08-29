from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LeagueTable

@admin.register(LeagueTable)
class LeagueTableAdmin(admin.ModelAdmin):
    list_display = ("id", "team", "points", "goals_scored", "goals_conceded")
    search_fields = ("team__name",)
