from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido a tu primera Web con Django</h1") # recibe una respuesta
def nosotros(request):
    return render(request, 'paginas/nosotros.html') #renderiza la página para utilizar y mostrar
