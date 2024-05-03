from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html') # recibe una respuesta

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #renderiza la página para utilizar y mostrar

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros}) #renderiza la página para utilizar y mostrar

def crear_libros(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html',{'formulario': formulario } ) #renderiza la página para utilizar y mostrar

def editar_libros(request, id):
    libro = Libro.objects.get(id = id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario }) #renderiza la página para utilizar y mostrar

def eliminar(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('libros')
