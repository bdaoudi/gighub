from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Gig(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)
    venue = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.venue

    def get_absolute_url(self):
        return reverse("gigs:detail", kwargs={"pk": self.pk})
