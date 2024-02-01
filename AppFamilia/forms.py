from django import forms
from AppFamilia.models import Familia

class CargaFormulario(forms.ModelForm):
    class Meta:
        model = Familia
        campos = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']   
        
         
    
    