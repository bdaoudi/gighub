from django import forms
from .models import Gig


class GigModelForm(forms.ModelForm):
    dateTime = forms.SplitDateTimeField()

    class Meta:
        model = Gig
        fields = "__all__"
