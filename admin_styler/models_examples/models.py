from __future__ import unicode_literals

from django.db import models

class Athlete(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
