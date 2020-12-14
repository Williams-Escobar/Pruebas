from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Pelicula, Categoria
from .forms import PeliculaForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

def post_list(request):
    return render(request, 'peliculas/base.html', {'publicacion':'publicacion'})

def categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'peliculas/categorias.html', {'categorias':categorias})

@login_required
def categoria_nuevo(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
    return render(request, 'peliculas/categoria_edit.html', {'form': form})

@login_required
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'peliculas/categoria_edit.html', {'form': form})

@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('categorias')

def pelicula_list(request):
    peliculas = Pelicula.objects.filter(fecha_Creacion__lte=timezone.now()).order_by('fecha_Creacion')
    return render(request, 'peliculas/listPeliculas.html', {'peliculas':peliculas})

@login_required
def create_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            return redirect('pelicula_list')
    else:
        formulario = PeliculaForm()
    return render(request, 'peliculas/newPelicula.html', {'form': formulario})

@login_required
def edit_pelicula(request,pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        formulario = PeliculaForm(request.POST, instance=pelicula)
        if formulario.is_valid():
            pelicula = formulario.save(commit=False)
            pelicula.save()
            return redirect('pelicula_list')
    else:
        formulario = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/newPelicula.html', {'form': formulario})
    
@login_required
def delete_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    pelicula.delete()
    return redirect('pelicula_list')

@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("henryjosue.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
