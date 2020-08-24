from django.db import models

class Meeting(models.Model):
    time = models.CharField(max_length=100)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    team3 = models.CharField(max_length=100)
