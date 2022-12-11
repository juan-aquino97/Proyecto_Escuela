from django import forms


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    profesion = forms.CharField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)
    camada = forms.IntegerField()
