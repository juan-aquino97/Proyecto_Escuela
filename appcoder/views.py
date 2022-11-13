from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.forms import ProfesorFormulario
from appcoder.models import Profesor
# Create your views here.

def inicio(request):
    return render(request, r"appcoder\index.html")


def cursos(request):
    return render(request, r"appcoder\cursos.html")


def estudiantes(request):
    return render(request, r"appcoder\estudiantes.html")


def profesores(request):
    return render(request, r"appcoder\profesores.html")


def entregables(request):
    return render(request, r"appcoder\entregables.html")

#Creacion de formularios

#Metodo 1
def creacion_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, r"appcoder/curso_formulario.html")

#Metodo 2
def creacion_profesores(request):
    if request.method == "POST":
        
        formulario = ProfesorFormulario(request.POST)
        
        if formulario.is_valid():
            
            info_profesor = formulario.cleaned_data
            
            profesor= Profesor(nombre=info_profesor["nombre"], apellido=info_profesor["apellido"], email=info_profesor["email"], profesion=info_profesor["profesion"])

            profesor.save()
            
        return render(request, r"appcoder/index.html")

    else:
        formulario = ProfesorFormulario()

    contexto = {"formulario": formulario}
    return render(request, r"appcoder/profesores_formularios.html", contexto)