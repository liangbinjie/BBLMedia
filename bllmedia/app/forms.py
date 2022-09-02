from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Contacto

class ContactoForms(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["email"]
