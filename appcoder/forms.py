from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    profesion = forms.CharField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)
    camada = forms.IntegerField()

class UserRegForm(UserCreationForm):
    email = forms.EmailField(label="Correo electronico")
    pasword1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "last_name", "password1", "password2"]   

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electronico")
    pasword1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required = False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, required = False)
    
    class Meta:
        model=User
        fields =["email", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField()