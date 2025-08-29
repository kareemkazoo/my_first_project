from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "position", "goals", "team")
    list_filter = ("position", "team")
    search_fields = ("name",)
