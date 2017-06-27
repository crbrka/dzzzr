from django import forms
from .models import *
#from olympic.models import *


class LoginAdminForm(forms.ModelForm):
    class Meta:
        model = GameAdmins
        exclude = ["created", "id", "name", "game"]


