from django.db import models

# Create your models here.
from django.db import models
from teams.models import Team

class LeagueTable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.points} pts"
