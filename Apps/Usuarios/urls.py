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
from Apps.Usuarios import views as views_usuarios

urlpatterns = [
    path('', views_usuarios.home, name = 'home'),
    path('loginn', views_usuarios.loginn, name = 'loginn'),
    path('register', views_usuarios.register, name='register'),
    path('cerrarsesion', views_usuarios.cerrar_sesion, name='cerrar_sesion')
]
