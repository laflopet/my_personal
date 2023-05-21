from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def inicio_app(request):
    return render(request, 'nav/inicio.html')

def acercade(request):
    return render(request, 'nav/acercademi.html')