from django.db import models

class pregunta(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)

class videojuegos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)


class libros(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)


class estudio(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    
from django.contrib.auth.models import User
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

def __str__(self):
    return f"{self.user} - {self.imagen}"

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=2200)

    def __str__(self):
        return f"{self.usuario}"


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    epigrafe = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.epigrafe}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=2200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.autor}: '{self.post}'"