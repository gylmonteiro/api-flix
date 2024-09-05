# from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Genero
# Create your views here.

@csrf_exempt
def generos_view(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        generos_dict = [{'id':genero.id, 'nome': genero.nome} for genero in generos]
        return JsonResponse(generos_dict, safe=False)
    elif request.method == 'POST':
        dados = json.loads(request.body.decode('utf-8'))
        novo_genero = Genero(nome=dados['nome'])
        novo_genero.save()
        return JsonResponse({'id': novo_genero.id, 'nome':novo_genero.nome}, status=201)

