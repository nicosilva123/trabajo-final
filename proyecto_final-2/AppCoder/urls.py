from django.urls import path
from django.contrib.auth.views import LogoutView

from AppCoder.views import (
    Lista_todo,
    inicio_view,
    juegos_buscar_view,
    crea_juego,
    eliminar_juego,
    editar_juegos,
    juego,
    crea_libro,
    libro_buscar,
    eliminar_libro,
    editar_libro,
    crea_estudio,
    estudioBuscar,
    eliminar_estudio,
    editar_estudio,
    registro_view,
    login_view,
    editar_perfil_view,
    crear_avatar_view,
    libro,
    estudioo,
    acerca_de_mi,
    preguntar_vd,
    preguntar_libro,
    preguntar_estudio
    )


app_name = "AppCoder"

urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("leer_todo/",Lista_todo, name="leer_todo"),
    path("juegos_buscar", juegos_buscar_view, name="juegos_buscar"),
    path("juego/<int:id>", juego, name="juego"),
    path("libro/<int:id>", libro, name="libro"),
    path("estudioo/<int:id>", estudioo, name="estudioo"),
    path("crea_juego/", crea_juego.as_view(), name="crea_juego"),
    path("eliminar_juego/<pk>", eliminar_juego.as_view(), name="eliminar_juego"),
    path("editar_juego/<pk>", editar_juegos.as_view(), name="editar_juego"),
    path("crea_libro/", crea_libro.as_view(), name="crea_libro"),
    path("libro_buscar", libro_buscar, name="libro_buscar"),
    path("eliminar_libro/<pk>", eliminar_libro.as_view(), name="eliminar_libro"),
    path("editar_libro/<pk>", editar_libro.as_view(), name="editar_libro"),
    path("crea_estudio/", crea_estudio.as_view(), name="crea_estudio"),
    path("estudioBuscar", estudioBuscar, name="estudioBuscar"),
    path("eliminar_estudio/<pk>", eliminar_estudio.as_view(), name="eliminar_estudio"),
    path("editar_estudio/<pk>", editar_estudio.as_view(), name="editar_estudio"),
    
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    
    path("editar-perfil", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar", crear_avatar_view, name="crear-avatar"),
    path("acerca_de_mi/", acerca_de_mi, name="acerca_de_mi"),
    path("preguntar_vd/<int:id>", preguntar_vd, name="preguntar_vd"),
    path("preguntar_libro/<int:id>", preguntar_libro, name="preguntar_libro"),
    path("preguntar_estudio/<int:id>", preguntar_estudio, name="preguntar_estudio"),
]
