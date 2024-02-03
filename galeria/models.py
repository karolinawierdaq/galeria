from django.conf import settings
from django.db import models
from django.utils import timezone

class Galeria(models.Model):
    nazwa = models.CharField(max_length=100)
    tekst = models.TextField()

    def __str__(self):
        return self.nazwa
