from django.shortcuts import render
from rest_framework import viewsets
from receita.models import Receitas
from .Serializers import ReceitasSerializers

class ReceitasViewSet(viewsets.ModelViewSet):
    '''Exibir todas as receitas'''
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializers
