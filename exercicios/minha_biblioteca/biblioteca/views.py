from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'biblioteca/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'biblioteca/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
from .models import Usuario, Livro, Autor, Categoria

def livros_por_usuario(request):
    
    contagem_livros = Usuario.objects.annotate(num_livros=Count('livro')).order_by('-num_livros')
    return render(request, 'biblioteca/livros_por_usuario.html', {'contagem_livros': contagem_livros})

def livros_por_autor(request, autor_id):
    
    autor = Autor.objects.get(id=autor_id)
    livros_autor = Livro.objects.filter(autor=autor)
    return render(request, 'biblioteca/livros_por_autor.html', {'autor': autor, 'livros_autor': livros_autor})

def livros_por_categoria(request, categoria_id):
    #
    categoria = Categoria.objects.get(id=categoria_id)
    livros_categoria = Livro.objects.filter(categoria=categoria)
    return render(request, 'biblioteca/livros_por_categoria.html', {'categoria': categoria, 'livros_categoria': livros_categoria})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'biblioteca/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')