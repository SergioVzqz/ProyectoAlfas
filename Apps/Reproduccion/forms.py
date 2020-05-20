from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, min_length = 5, required = True, widget = forms.TextInput())
    password = forms.CharField(max_length = 50, min_length = 5, required = True, widget = forms.TextInput())