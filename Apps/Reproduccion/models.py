from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User


def images_path():
    return os.path.join(settings.STATICFILES_DIRS, 'img/disc_photos')

# Create your models here.


class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DecimalField(max_digits=4, decimal_places=2)
    autor = models.CharField(max_length=100)
    calificacion = models.DecimalField(
        max_digits=4, decimal_places=2, null=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)


class Album(models.Model):
    nombre = models.CharField(max_length=60)
    duracion = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    foto = models.ImageField(upload_to=images_path, max_length=100)


class Disquera(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120, null=True)


class Generos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True)


class Playlist(models.Model):
    is_public = models.BooleanField()
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class PlaylistCanciones(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE)

class UsuarioCanciones(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE)
