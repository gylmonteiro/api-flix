# from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
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

@csrf_exempt
def detalhar_genero_view(request, pk):
	genero = get_object_or_404(Genero,pk=pk)
	dados = {'id':genero.id, 'nome': genero.nome}
	return JsonResponse(dados)

@csrf_exempt
def atualizar_genero_view(request,pk):
     genero = get_object_or_404(Genero, pk=pk)
     dados = json.loads(request.body.decode('utf-8'))['nome']
     genero.nome = dados
     genero.save()
     return JsonResponse({'id': genero.id, 'nome': genero.nome})