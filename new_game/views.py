from django.shortcuts import render, redirect
from new_game.forms import *

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
    nivel = objJogo.nivel_jogo
    desafios = None
    if nivel == "f":
        desafios = Desafios.objects.filter(nivel_frase = "f")
    elif nivel == "m":
        desafios = Desafios.objects.filter(nivel_frase = "m")
    elif nivel == "d":
        desafios = Desafios.objects.filter(nivel_frase = "d")
    else:
        desafios = Desafios.objects.all()
    context = {
        "nome_pagina":"jogo rolando",
        "objJogo": objJogo,
        "desafios" : desafios
    }

    return render(request,"inicio_jogo.html",context)

