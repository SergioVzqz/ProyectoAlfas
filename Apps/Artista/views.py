from django.shortcuts import render, HttpResponse, redirect
from Apps.Reproduccion.models import Album, Cancion, Genero
import json
# Create your views here.


def home_artista(request):
    return render(request, 'home_artista.html')


def albums(request):
    canciones = Cancion.objects.filter(album__artista=request.user)
    return render(request, 'album_artista.html', {
        'canciones': canciones
    })


def nuevo_album(request):
    return render(request, 'nuevo_album.html')


def editar_album(request, idAlbum):
    canciones = Cancion.objects.filter(album__id=idAlbum)
    return render(request, 'editar_album.html', {
        'canciones': canciones,
        'idAlbum': idAlbum
    })


def perfil_artista(request):
    return render(request, 'perfil_artista.html')


def cambiar_password(request):
    return render(request, 'cambiar_password.html')


def actualizar_album(request):
    datos = json.loads(request.body)
    idAlbum = int(datos['idAlbum'])
    fechaAlbum = datos['fechaAlbum']
    generoAlbum = datos['generoAlbum']
    nombreAlbum = datos['nombreAlbum']

    try:
        album = Album.objects.get(id=idAlbum)
        album.fecha = fechaAlbum

        album.nombre = nombreAlbum
        genero_nuevo, fueCreado = Genero.objects.get_or_create(
            nombre=generoAlbum)
        album.genero = genero_nuevo
        album.save()
        return HttpResponse(True)

    except Exception as identifier:
        print(identifier)
        return HttpResponse(False)

    
def eliminar_album(request):
    idAlbum = int(json.loads(request.body))
    print(idAlbum)


    try:
        album = Album.objects.get(id=idAlbum)
        album.delete()
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)
    