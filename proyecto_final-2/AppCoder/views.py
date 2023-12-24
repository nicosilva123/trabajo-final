from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import *

from .forms import *

from django.contrib.auth.decorators import login_required

def acerca_de_mi(request):
    return render(request, "AppCoder/acerca_de_mi.html")

def preguntar_vd(request, id):
    data = {
        "videojuegos" : videojuegos.objects.get(id=id)
    }
    return render(request, "AppCoder/preguntar_vd.html", data)

def preguntar_libro(request, id):
    data = {
        "libros" : libros.objects.get(id=id)
    }
    return render(request, "AppCoder/preguntar_libro.html", data)

def preguntar_estudio(request, id):
    data = {
        "estudio" : estudio.objects.get(id=id)
    }
    return render(request, "AppCoder/preguntar_estudio.html", data)

def juego(request, id):
    data = {
        "videojuegos" : videojuegos.objects.get(id=id)
    }
    return render(request, "AppCoder/juego.html", data)

def libro(request, id):
    data = {
        "libros" : libros.objects.get(id=id)
    }
    return render(request, "AppCoder/libro.html", data)

def estudioo(request, id):
    data = {
        "estudio" : estudio.objects.get(id=id)
    }
    return render(request, "AppCoder/estudioo.html", data)

@login_required
def Lista_todo(request):
    Juegos = videojuegos.objects.all()
    Libros = libros.objects.all()
    Estudio = estudio.objects.all()
    return render(request, "AppCoder/leer_todo.html", {"videojuegos":Juegos,"libros":Libros,"estudio":Estudio})

def inicio_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""

    return render(request, "AppCoder/inicio.html", context={"avatar_url": avatar_url})
    

def juegos_buscar_view(request):
    if request.method == "GET":
        form = juegosBuscarFormulario()
        return render(
            request,
            "AppCoder/juego_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = juegosBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            juegos_filtrados = []
            for juego in videojuegos.objects.filter(titulo=informacion["titulo"]):
                juegos_filtrados.append(juego)

            contexto = {"videojuegos": juegos_filtrados}         
            return render(request, "AppCoder/leer_todo.html", contexto)
    
def libro_buscar(request):
    if request.method == "GET":
        form = librosBuscarFormulario()
        return render(
            request,
            "AppCoder/libro_buscar.html",
            context={"form": form}
        )
    else:
        formulario = librosBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            libros_filtrados = []
            for titulo in libros.objects.filter(titulo=informacion["titulo"]):
                libros_filtrados.append(titulo)

            contexto = {"libros": libros_filtrados}         
            return render(request, "AppCoder/leer_todo.html", contexto)
        
    
def estudioBuscar(request):
    if request.method == "GET":
        form = estudioBuscarFormulario()
        return render(
            request,
            "AppCoder/estudioBuscar.html",
            context={"form": form}
        )
    else:
        formulario = estudioBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudios_filtados = []
            for titulo in estudio.objects.filter(titulo=informacion["titulo"]):
                estudios_filtados.append(titulo)

            contexto = {"estudio": estudios_filtados}         
            return render(request, "AppCoder/leer_todo.html", contexto)


from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class crea_juego(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = videojuegos
    template_name = "AppCoder/juegoFormulario.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
    success_message = "Juego creado con éxito!" 
    
class editar_juegos(LoginRequiredMixin, UpdateView):
    model = videojuegos
    template_name = "AppCoder/editarJuego.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
  
class eliminar_juego(LoginRequiredMixin, DeleteView):
    model = videojuegos
    template_name = "AppCoder/eliminar_juego.html"
    success_url = reverse_lazy("AppCoder:leer_todo")

class crea_libro(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = libros
    template_name = "AppCoder/libroFormulario.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
    success_message = "Libro creado con éxito!" 
    
class editar_libro(LoginRequiredMixin, UpdateView):
    model = libros
    template_name = "AppCoder/editarlibro.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
    
class eliminar_libro(LoginRequiredMixin, DeleteView):
    model = libros
    template_name = "AppCoder/eliminar_libro.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    
class crea_estudio(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = estudio
    template_name = "AppCoder/estudioFormulario.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
    success_message = "Estudio creado con éxito!" 
    
class editar_estudio(LoginRequiredMixin, UpdateView):
    model = estudio
    template_name = "AppCoder/editarEstudio.html"
    success_url = reverse_lazy("AppCoder:leer_todo")
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha"]
    
class eliminar_estudio(LoginRequiredMixin, DeleteView):
    model = estudio
    template_name = "AppCoder/eliminar_estudio.html"
    success_url = reverse_lazy("AppCoder:leer_todo")


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )

def logout_view(request):
    pass

from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView

def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "AppCoder/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "AppCoder/registro.html",
                {"form": formulario}
            )



from django.contrib.auth.decorators import login_required

@login_required
def editar_perfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""


    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "AppCoder/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("AppCoder:inicio")

@login_required
def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "AppCoder/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("AppCoder:inicio")