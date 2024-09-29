from django.contrib import admin
from .models import Categoria, Receitas, Avaliação

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Receitas)
admin.site.register(Avaliação)