from django import forms

from .models import Panda_Geant

class PandaForm(forms.ModelForm):

    class Meta:
        model = Panda_Geant
        fields = '__all__'