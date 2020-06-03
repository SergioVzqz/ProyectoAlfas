"""ProyectoAlfas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Apps.Artista import views as views_artista

urlpatterns = [
    path('', views_artista.home_artista, name='home_artista'),
    path('albums/', views_artista.albums, name='albums'),
    path('albums/nuevo/', views_artista.nuevo_album, name='nuevo_album'),
    path('albums/editar/<int:idAlbum>',
         views_artista.editar_album, name='editar_album'),
    path('perfil_artista/', views_artista.perfil_artista, name='perfil_artista'),
    path('cambiar_password/', views_artista.cambiar_password,
         name='cambiar_password'),
    path('albums/update', views_artista.actualizar_album, name='actualizar_album'),
    path('albums/delete', views_artista.eliminar_album, name='eliminar_album'),
    path('albums/nuevo/add', views_artista.agregar_album, name='agregar_album'),
    path('cancion/add', views_artista.agregar_cancion, name='agregar_cancion'),
    path('cancion/delete', views_artista.eliminar_cancion, name='eliminar_cancion'),
    path('cancion/update', views_artista.actualizar_cancion, name='actualizar_cancion'),

]
