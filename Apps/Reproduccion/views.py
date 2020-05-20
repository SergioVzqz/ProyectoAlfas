from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# HTTPRESPONSE, JSONRESPONSE, RENDER

# Create your views here.
def home(request):
    form = LoginForm()
    return render(request, 'repro_home.html', {'form':form})