# from django.shortcuts import render
from django.http import JsonResponse
from .models import Genero
# Create your views here.


def generos_view(request):
    generos = Genero.objects.all()
    generos_dict = [{'id':genero.id, 'nome': genero.nome} for genero in generos]

    return JsonResponse(generos_dict, safe=False)