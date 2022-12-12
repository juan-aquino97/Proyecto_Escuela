from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} -> Camada: {self.camada}" 
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)


class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

class Avatars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)