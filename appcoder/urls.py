from django.urls import path
from appcoder import views

urlpatterns = [
    path("", views.inicio, name="coder-inicio"),

    path("estudiantes/", views.estudiantes, name="coder-estudiantes"),
    
    path("profesores/", views.profesores, name="coder-profesores"),

    path("profesores/crear/", views.creacion_profesores, name="coder-profesores-crear"),
    
    path("cursos/", views.cursos,name="coder-cursos"),

    path("cursos/crear/", views.creacion_curso, name="coder-cursos-crear"),
    
    path("entregables/", views.entregables,name="coder-entregables"),
]