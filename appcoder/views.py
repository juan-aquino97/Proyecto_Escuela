from django.shortcuts import render, redirect
from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.forms import *
from appcoder.models import *
from ProyectoEscuela.settings import BASE_DIR
import os
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
#Logins
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        imagen_model=Avatars.objects.filter(user= request.user.id).order_by("-id")[0]    
        imagen_url= imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, r"appcoder\index.html", {"imagen_url": imagen_url})

@login_required
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


class EntregablesList(LoginRequiredMixin, ListView):
    
    model = Entregable
    template_name = "appcoder/list_entregables.html"

class EntregableDetail(DetailView):

    model = Entregable
    template_name = "appcoder/detail_entregable.html" 

class EntregableCreate(CreateView):
    model = Entregable
    succes_url ="/coder/cursos/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]

def iniciar_sesion(request):
    errors = []

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("coder-inicio")
            else:
                return render(request,"appcoder/login.html", {"form": formulario, "errors": "Credenciales inválidas"})
        else:
            return render(request, "appcoder/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "appcoder/login.html", {"form": formulario, "errors": errors})


def registrar_usuario(request):

    if request.method == "POST":    
        formulario = UserRegForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect("coder-inicio")
        else:
            return render(request, "appcoder/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegForm()
    return render(request,"appcoder/register.html", {"form": formulario})
    

@login_required
def editar_perfil(request):
    usuario = User

    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.isvalid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.last_name["last_name"]

            usuario.save()
            return redirect("coder-inicio")
        else:
            return render(request,"appcoder/editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        formulario = UserEditForm(initial = {"email": usuario.email, "last_name": usuario.last_name})
    return render(request,"appcoder/editar_perfil.html", {"form": formulario})


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatars(user=usuario, imagen=data["imagen"])
            avatar.save()
            return redirect('coder-inicio')
        else:
            return render(request, "appcoder/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})
    formulario= AvatarForm()
    return render(request, "appcoder/agregar_avatar.html", {"form": formulario})
