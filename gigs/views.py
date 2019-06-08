from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Gig
from .forms import GigModelForm
from django.contrib.auth.mixins import LoginRequiredMixin


class GigCreate(LoginRequiredMixin, CreateView):
    form_class = GigModelForm
    template_name = "gigs/gig_form.html"
    # fields = ['artist', 'venue', 'genre', 'dateTime']

    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add a gig"
        return context


class GigDetail(DetailView):
    model = Gig


class GigList(ListView):
    model = Gig


class GigUpdate(LoginRequiredMixin, UpdateView):
    form_class = GigModelForm
    template_name = "gigs/gig_form.html"
    queryset = Gig.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update the gig"
        return context
