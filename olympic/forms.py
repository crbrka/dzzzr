from django import forms
from .models import *

class LoginTeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        exclude=["created","updated","name","game"]


class CodeEnterForm(forms.ModelForm):
    class Meta:
        model = Codes
        exclude=["team","game","created","ip_addr","client"]