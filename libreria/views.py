from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html') # recibe una respuesta

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #renderiza la página para utilizar y mostrar

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros}) #renderiza la página para utilizar y mostrar

def crear_libros(request):
    return render(request, 'libros/crear.html') #renderiza la página para utilizar y mostrar

def editar_libros(request):
    return render(request, 'libros/editar.html') #renderiza la página para utilizar y mostrar