from django.template import loader, Template, Context
from django.http import HttpResponse
from AppFamilia.models import Familia
from AppFamilia.models import CargaFormulario 
from django.shortcuts import render, redirect


def registro(request):
    registro = Familia(nombre="Juan Pablo", apellido="Luna", edad=46, fecha_nacimiento="1977-12-02")
    registro1 = Familia(nombre="Erica", apellido="Briglia", edad=46, fecha_nacimiento="1978-04-25")
    registro2 = Familia(nombre="Facundo", apellido="Luna Briglia", edad=18, fecha_nacimiento="2006-01-25")
    registro3 = Familia(nombre="Ignacio", apellido="Luna Briglia", edad=14, fecha_nacimiento="2009-07-15")
    registro.save()
    registro1.save()
    registro2.save()
    registro3.save()
    
    return HttpResponse("Registro exitoso")


def cargar_datos(request):
    if request.method == "POST":
        form = CargaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CargaFormulario()
    return render(request, 'carga_datos.html', {'form': form})
        

    
    
     