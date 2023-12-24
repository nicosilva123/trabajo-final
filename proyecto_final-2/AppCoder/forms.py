from django import forms
from .models import Avatar

class pregunta(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    cuerpo = forms.CharField()

class juegosFormulario(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.CharField()
    
class juegosBuscarFormulario(forms.Form):
    titulo = forms.CharField()
    
    
class librosFromulario(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.CharField()
    
class librosBuscarFormulario(forms.Form):
    titulo = forms.CharField()
    
class estudioFormulario(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.CharField()
    
class estudioBuscarFormulario(forms.Form):
    titulo = forms.CharField()
    
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}


class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]
