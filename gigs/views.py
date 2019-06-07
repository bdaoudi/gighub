from django.shortcuts import render
from django.views.generic import CreateView
from .models import Gig


class GigCreateView(CreateView):
    model = Gig
    fields = ['artist', 'venue', 'genre', 'dateTime']
