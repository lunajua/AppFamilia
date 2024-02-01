from django.db import models
from django import forms

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()  
    
class CargaFormulario(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']   
            