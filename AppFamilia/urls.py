from django.urls import path
from AppFamilia.views import cargar_datos

urlpatterns = [
    path("index/", cargar_datos, name="index"),
               
]