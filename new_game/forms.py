from django import forms
from new_game.models import *

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'

class JogadorForm(forms.ModelForm):
    class Meta: 
        model = Jogador
        fields = ["nome_completo"]