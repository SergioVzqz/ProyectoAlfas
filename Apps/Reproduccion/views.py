from django.shortcuts import render, HttpResponse
from .models import Cancion
from django.db.models import Q
from django.http import JsonResponse

# HTTPRESPONSE, JSONRESPONSE, RENDER

# Create your views here.


def home(request):
    canciones = Cancion.objects.all()
    return render(request, 'home_rep.html', {
        'canciones': canciones
    })


def busqueda(request):
    texto = request.POST['texto']
    if texto != "":
        canciones = Cancion.objects.filter(
            Q(nombre__icontains=texto) |
            Q(autor__icontains=texto) |
            Q(album__nombre__icontains=texto) |
            Q(album__genero__icontains=texto) |
            Q(album__artista__username__icontains=texto)
        ).values_list('nombre', 'duracion', 'autor', 'album__nombre', 'archivo').order_by('album')

        lista = list(canciones)
        return JsonResponse({'lista': lista})
    else:
        canciones = Cancion.objects.all().values_list('nombre', 'duracion', 'autor',
                                                      'album__nombre', 'archivo').order_by('album')

        lista = list(canciones)
        return JsonResponse({'lista': lista})
