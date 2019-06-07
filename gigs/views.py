from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Gig
from .forms import GigModelForm


class GigCreate(CreateView):
    form_class = GigModelForm
    template_name = "gigs/gig_form.html"
    # fields = ['artist', 'venue', 'genre', 'dateTime']


class GigDetail(DetailView):
    model = Gig


class GigList(ListView):
    model = Gig


class GigUpdate(UpdateView):
    form_class = GigModelForm
    template_name = "gigs/gig_form.html"
    queryset = Gig.objects.all()
