from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "founded", "city")
    search_fields = ("name", "city")
