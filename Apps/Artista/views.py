from django.shortcuts import render, HttpResponse, redirect
from Apps.Reproduccion.models import Album, Cancion, Genero, Disquera
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_artista(request):
    return render(request, 'home_artista.html')

@login_required
def albums(request):
    album_artista = Album.objects.filter(artista = request.user).values('id')
    album_canciones = Cancion.objects.filter(album__artista=request.user).values('album')
    album_sin_canciones = album_artista.filter(~Q(id__in=album_canciones))
    albums = Album.objects.filter(id__in=album_sin_canciones)

    canciones = Cancion.objects.filter(
        album__artista=request.user).order_by('album')
    print(canciones)
    return render(request, 'album_artista.html', {
        'canciones': canciones,
        'albums': albums
    })


def nuevo_album(request):
    return render(request, 'nuevo_album.html')


def editar_album(request, idAlbum):
    album = Album.objects.get(id=idAlbum)
    canciones = Cancion.objects.filter(album__id=idAlbum)
    return render(request, 'editar_album.html', {
        'canciones': canciones,
        'idAlbum': idAlbum,
        'album': album
    })

@login_required
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

    try:
        album = Album.objects.get(id=idAlbum)
        album.delete()
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)


def agregar_cancion(request):
    nombreCancion = request.POST['nombreCancion']
    duracionCancion = request.POST['duracionCancion']
    autorCancion = request.POST['autorCancion']
    idAlbum = request.POST['idAlbum']
    archivoCancion = request.FILES['archivoCancion']
    print(nombreCancion, duracionCancion,
          autorCancion, idAlbum, archivoCancion)

    try:
        Cancion.objects.create(
            nombre=nombreCancion,
            duracion=duracionCancion,
            autor=autorCancion,
            album_id=idAlbum,
            archivo=archivoCancion

        )
        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(False)


def eliminar_cancion(request):
    try:
        idCancion = request.POST['idCancion']
        cancion = Cancion.objects.get(id=idCancion)
        cancion.delete()
        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(False)


def actualizar_cancion(request):
    try:
        idCancion = request.POST['idCancion']
        cancion = Cancion.objects.get(id=idCancion)
        cancion.nombre = request.POST['nombreCancion']
        cancion.duracion = request.POST['idCancion']
        cancion.autor = request.POST['autorCancion']
        cancion.save()
        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(False)


def agregar_album(request):
    try:
        nombreAlbum = request.POST['nombreAlbum']
        fechaAlbum = request.POST['fechaAlbum']
        disqueraAlbum = request.POST['disqueraAlbum']
        generoAlbum = request.POST['generoAlbum']
        fotoAlbum = request.FILES['fotoAlbum']
        numeroCanciones = int(request.POST['numeroCanciones'])+1

        canciones = []
        for x in range(0, numeroCanciones):
            numero = str(x)
            canciones.append(request.FILES['cancion['+numero+']'])

        genero, createdGenero = Genero.objects.get_or_create(
            nombre=generoAlbum)
        disquera, createdDisquera = Disquera.objects.get_or_create(
            nombre=disqueraAlbum)
            
        album_nuevo = Album.objects.create(
            nombre=nombreAlbum,
            fecha=fechaAlbum,
            disquera=disquera,
            genero=genero,
            foto=fotoAlbum,
            artista=request.user
        )

        for cancion in canciones:
            name = cancion.name
            name = name.split(".")[0]
            Cancion.objects.create(
                nombre=name,
                duracion=1.00,
                autor=request.user,
                album=album_nuevo,
                archivo=cancion
            )

        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(error)
