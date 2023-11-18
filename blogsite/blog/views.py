
from django.shortcuts import render, get_object_or_404
from .models import Publicacion

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def blog_home(request):
    publicaciones = Publicacion.objects.all()
    ultima_publicacion = Publicacion.objects.latest('fecha_publicacion')
    return render(request, 'blog/blog_home.html', {'publicaciones': publicaciones, 'ultima_publicacion': ultima_publicacion})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})