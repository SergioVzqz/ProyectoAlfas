from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# HTTPRESPONSE, JSONRESPONSE, RENDER

# Create your views here.
def home(request):
    

    if request.method == 'POST':
        formS = LoginForm(request.POST)
        if formS.is_valid():
            username = formS.cleaned_data['username']
            password = formS.cleaned_data['password']
            print(username)
            print(password)
            return HttpResponse(username)
        else:
            return HttpResponse('Revisa tu formulario')


    else:
        form = LoginForm()
        return render(request, 'repro_home.html', {'form':form})