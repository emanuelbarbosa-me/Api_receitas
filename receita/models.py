from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=True)

class Receitas(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(max_length=255, blank=True)
    ingredientes = models.TextField(max_length=255, blank=True)
    modo_preparo = models.TextField(max_length=255, blank=True)
    tempo_de_preparo = models.TimeField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criação = models.DateField(null=True)
    publico_privado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Avaliação(models.Model):
    receitas = models.ForeignKey(Receitas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    Comentarios = models.TextField(max_length=255, blank=False)

    def __str__(self) -> str:
        return f'{self.usuario} ({self.nota})'
