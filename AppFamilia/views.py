from django.shortcuts import render, redirect
from AppFamilia.models import CargaFormulario

# def cargar_datos(request):
#     if request.method == "POST":
#         form = CargaFormulario(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CargaFormulario()
#     return render(request, 'carga_datos.html', {'form': form})

def autor_create_view(request):
    form = CargaFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        form = CargaFormulario()
        template_index = 'index.html'
        context = {'form':form}
        return render(request, template_index,context)
    else:
        form = CargaFormulario()
        return render(request, 'index.html', {'form':form})