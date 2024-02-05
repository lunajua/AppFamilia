from django.contrib import admin
from django.urls import path, include
from Proyecto_Clase18.views import registro
from AppFamilia.views import cargar_datos



urlpatterns = [
    path("admin/", admin.site.urls),
    path("registro/", registro),
    path("cargar_datos", cargar_datos),  
    path("AppFamilia/", include("AppFamilia.urls")),  
    
]
