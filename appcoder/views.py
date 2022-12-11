from django.shortcuts import render, redirect
from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.forms import *
from appcoder.models import *
from ProyectoEscuela.settings import BASE_DIR
import os
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    return render(request, r"appcoder\index.html")


def cursos(request):
    errores = ""

    # Validamos tipo de peticion
    if request.method == "POST":
        # Cargamos los datos en el formulario
        formulario = CursoFormulario(request.POST)

        # Validamos los datos
        if formulario.is_valid():
            # Recuperamos los datos sanitizados
            data = formulario.cleaned_data
            # Creamos el curso
            curso = Curso(nombre=data["nombre"], camada=data["camada"])
            # Guardamos el curso
            curso.save()
        else:
            # Si el formulario no es valido, guardamos los errores para mostrarlos
            errores = formulario.errors

    # Recuperar todos los cursos de la BD
    cursos = Curso.objects.all() # Obtener TODOS los registros de ese modelo
    
    # Creamos el formulario vacio
    formulario = CursoFormulario()
    
    # Creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": errores}
    
    # Retornamos la respuesta
    return render(request, "appcoder/cursos.html", contexto)



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


    #Búsqueda con form

def busqueda_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")

def resultado_busqueda_cursos(request):
    
    nombre_curso =  request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request,"appcoder/res_bus_cursos.html", {"cursos": cursos})

def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":
        formulario= CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request,"appcoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": ""})


class EntregablesList(ListView):
    model = Entregable
    template_name = "appcoder/list_entregables.html"

class EntregableDetail(DetailView):

    model = Entregable
    template_name = "appcoder/detail_entregable.html" 

class EntregableCreate(CreateView):
    model = Entregable
    succes_url ="/coder/cursos/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]