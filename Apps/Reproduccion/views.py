from django.shortcuts import render, HttpResponse

# HTTPRESPONSE, JSONRESPONSE, RENDER

# Create your views here.
def home(request):
    return render(request, 'home_rep.html')
