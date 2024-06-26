from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()

    # tem que relacionar livro ao usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
