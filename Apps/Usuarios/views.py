from django.shortcuts import render

# Create your views here.
def renderizado(request):
    print('Prueba')
    return render(request, 'index.html')
    