from django.urls import path
from AppFamilia.views import autor_create_view

urlpatterns = [path("index/", autor_create_view)]