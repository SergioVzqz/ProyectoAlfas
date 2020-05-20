from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Ingresa tu usuario', max_length = 50, min_length = 5, required = True, widget = forms.TextInput(attrs={'placeholder' : 'Ingresa tu usuario', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña',max_length = 50, min_length = 5, required = True, widget = forms.PasswordInput(attrs={'placeholder' : 'Ingresa tu contraseña','class' : 'form-control'}))