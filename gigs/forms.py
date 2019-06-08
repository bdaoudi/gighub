from django import forms
from .models import Gig, Genre
from django.contrib.auth.models import User


class GigModelForm(forms.ModelForm):
    dateTime = forms.SplitDateTimeField(label="", widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date', 'class': 'form-control col-4'},
        time_attrs={'type': 'time', 'class': 'form-control col-4 mt-1'}),
        help_text="Date format: dd/mm/yyyy \nTime format: hh:MM")
    venue = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'col-6',
                                                'placeholder': 'Venue'}),
        help_text="Provide a description for your venue")
    genre = forms.ModelChoiceField(
        label="", empty_label="--- Select a genre ---",
        queryset=Genre.objects.all(),
        widget=forms.Select(attrs={'class': 'col-6'}))
    # artist = forms.ModelChoiceField(
    #     queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'col-6'}))

    class Meta:
        model = Gig
        fields = [
            'venue',
            'dateTime',
            'genre',
        ]
