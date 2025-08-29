from django.db import models

# Create your models here.
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    founded = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
