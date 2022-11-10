from django.urls import path
from appcoder import views

urlpatterns = [
    path("", views.inicio, name="coder-inicio"),
    path("estudiantes/", views.estudiantes, name="coder-estudiantes"),
    
    path("profesores/", views.profesores, name="coder-profesores"),
    
    path("cursos/", views.cursos,name="coder-cursos"),
    
    path("entregables/", views.entregables,name="coder-entregables"),
]