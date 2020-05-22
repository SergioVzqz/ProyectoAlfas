from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Ingresa tu usuario', max_length=50, min_length=5, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ingresa tu usuario', 'class': 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', max_length=50, min_length=5, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña', 'class': 'form-control'}))


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name',
                  'last_name', 'fechaNacimiento', 'pais', 'foto', 'is_artist']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el usuario deseado'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa una contraseña'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa un correo'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'}),

            'fechaNacimiento': forms.DateInput(format='%d,%m,%Y', attrs={'class': 'form-control', 'required': 'true','placeholder':'DD/MM/AAAA'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa un correo'}),


        }

        help_texts = {
            'username': 'Maximo 150 caracteres',
            'password': 'Minimo 8 caracteres'
        }
