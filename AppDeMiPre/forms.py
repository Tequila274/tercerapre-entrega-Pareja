from django import forms

class Alta_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    rol = forms.CharField(max_length=20)