
from AppFamilia.models import Familia
from django import forms


class CargaFormulario(forms.ModelForm):
    class Meta:
        model = Familia
        fields = "__all__"

         
    
    