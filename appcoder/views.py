from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso

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