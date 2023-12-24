from django.contrib import admin

from . import models


# Register your models here.

from .models import *


@admin.register(videojuegos)
class JuegosAdmin(admin.ModelAdmin):
    pass

@admin.register(libros)
class LibrosAdmin(admin.ModelAdmin):
    pass

@admin.register(estudio)
class EstudioAdmin(admin.ModelAdmin):
    pass