from django import forms

from .models import Temoignage

class TemoignageForm(forms.ModelForm):

    class Meta:
        model = Temoignage
        fields = ('titre', 'contenu',)