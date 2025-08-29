from django.db import models

# Create your models here.
from django.db import models
from teams.models import Team

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_matches")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_matches")
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"
