from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Gig, Attendance
from django.contrib.auth.models import User
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


class AttendAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):
        gig = get_object_or_404(Gig, id=id)
        user = request.user
        # if request.method == 'POST':
        data = {}
        is_attend = Attendance.objects.filter(attendee_id=user.id,
                                              gig_id=gig.id).exists()
        if is_attend:
            # gig.attendees.clear()
            Attendance.objects.filter(attendee_id=user.id,
                                      gig_id=gig.id).delete()
            is_attend = not is_attend
        else:
            Attendance.objects.create(attendee=user, gig=gig)
            is_attend = not is_attend
        data = {
            'is_attending': is_attend,
        }
        return Response(data)


class AttendAPICheck(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):
        gig = get_object_or_404(Gig, id=id)
        user = request.user
        # if request.method == 'POST':
        data = {}
        is_attend = Attendance.objects.filter(attendee_id=user.id,
                                              gig_id=gig.id).exists()
        data = {
            'is_attending': is_attend,
        }
        return Response(data)
