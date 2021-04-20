from django.shortcuts import render, redirect
from new_game.forms import *
import random
from rest_framework import *
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
    

def cadastrar_jogo(request):
    formJogo = JogoForm

    if request.method == "POST":

        form = JogoForm(request.POST)

        if form.is_valid():
            objJogo=form.save()
            

            listJogador = request.POST.getlist("Jogador[]", None)
            
            for x in range(len(listJogador)):
                objJogador = Jogador()
                objJogador.nome_completo = listJogador[x]
                objJogador.jogo = objJogo 
                objJogador.save()
            
            return redirect("inicio_jogo",objJogo.id)
                

    context = {
        "nome_pagina":"Cadastrar jogo",
        "formJogo":formJogo,
    }

    return render(request,"cadastro_jogo.html",context)


def inicio_jogo(request,id_jogo):
    objJogo = Jogo.objects.get(pk=id_jogo)
    listUsuarios = Jogador.objects.filter(jogo=objJogo)
    nivel = objJogo.nivel_jogo

    context = {
        "nome_pagina":objJogo.nome,
        "objJogo": objJogo,
        "id_jogo" :id_jogo,
        "listUsuarios":listUsuarios,
    }

    return render(request,"inicio_jogo.html",context)

def gerar_frase(request):
    nivel = request.GET.get("nivel",None)
    id_jogo = request.GET.get("id_jogo",None)
    user = request.GET.get("user",None)
    objJogo = Jogo.objects.get(pk=id_jogo)
    objJogador = Jogador.objects.get(jogo=objJogo,pk=user)
    
    if nivel != "xtd":
        desafios = Desafios.objects.filter(nivel_frase = nivel)
    else:
        desafios = Desafios.objects.all()    
    n = random.randint(0,(len(desafios)-1))

    doses = Qtd_doses.objects.all()    
    n2 = random.randint(0,(len(doses)-1))  

    data = {
        'Frase':desafios[n].frase,
        'doses':doses[n2].frase,
        'jogador':objJogador.nome_completo,
    }
    data_json = json.dumps(data,cls=DjangoJSONEncoder)
    return HttpResponse(data_json, content_type="application/json")

def gravar_ponto(request):
    ponto = request.GET.get('ponto',None)
    jogador = request.GET.get('jogador',None)
    print(jogador)
    objJogador = Jogador.objects.get(pk=jogador)
    objJogador.pontuacao += int(ponto)
    regra_da_casa = RegraCasa.objects.all()
    n = random.randint(0,(len(regra_da_casa)-1))


    objJogador.save()
    data ={
        "texto":"pontuaçao computada",
        "regra_casa":regra_da_casa[n].frase,
    }
    data_json = json.dumps(data,cls=DjangoJSONEncoder)
    return HttpResponse(data_json, content_type="application/json")


def sair(request,id_jogo):
    objJogo = Jogo.objects.get(pk=id_jogo)
    listUsuarios = Jogador.objects.filter(jogo=objJogo) 

    context = {
        "nome_pagina":"Arregão",
        "listUsuarios" : listUsuarios,
    }
    return render(request,"gerar_pdf.html",context)

