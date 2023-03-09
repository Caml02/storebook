from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.

def inicio(request): 
    return render(request, 'pages/inicio.html')
def nosotros(request):
    return render(request, 'pages/nosotros.html')

# books views

def books(request):
    books = Libro.objects.all()
    print(books)
    return render(request, 'books/index.html', {'books': books})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('books')
    return render(request, 'books/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('books')
    return render(request, 'books/editar.html', {'formulario': formulario})

def borrar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('books')
