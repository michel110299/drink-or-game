from django.contrib import admin
from django.urls import path
from new_game.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cadastrar_jogo,name='cadastrar_jogo',),
    path('inicio/<int:id_jogo>/',inicio_jogo,name='inicio_jogo',),
    path('gerar_frase/',gerar_frase, name='gerar_frase'),
    path('gravar_ponto/',gravar_ponto, name='gravar_ponto'),
    path('desistir/<int:id_jogo>/',sair, name='desistir'),
    path('certificado/<int:id_jogador>/<int:id_jogo>/',html_to_pdf_view,name='certificado'),



]


