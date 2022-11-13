from django import forms


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    profesion = forms.CharField()