from django.shortcuts import render, redirect
from .forms import CargaFormulario

def cargar_datos(request):
    if request.method == "POST":
        form = CargaFormulario(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CargaFormulario()
    return render(request, 'index.html', {'form': form})
    
def index(request):
    return render(request, 'index.html')