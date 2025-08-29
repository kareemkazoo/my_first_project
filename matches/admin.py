from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("id", "home_team", "away_team", "home_score", "away_score", "date")
    list_filter = ("date", "home_team", "away_team")
