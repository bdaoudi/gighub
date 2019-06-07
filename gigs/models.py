from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=150)


class Gig(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)
    venue = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
