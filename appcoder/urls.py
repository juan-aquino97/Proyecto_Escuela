from django.urls import path
from appcoder import views

urlpatterns = [
    path("", views.inicio),
    path("estudiantes/", views.estudiantes),
    
    path("profesores/", views.profesores),
    
    path("cursos/", views.cursos),
    
    path("entregables/", views.entregables),
]