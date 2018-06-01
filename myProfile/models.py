from __future__ import unicode_literals
from django.db import models

class ProgrammingLanguages(models.Model):
    langName = models.CharField(max_length=25)
    proficiency = models.PositiveSmallIntegerField()
    years = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.langName
