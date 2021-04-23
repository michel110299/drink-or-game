from django.db import models

NIVEL_JOGO=(
    ("f","Fácil"),
    ("m", "Médio"),
    ("d" , "Dificil"),
    ("xtd", "X-tudo"),
)
NIVEL_DESAFIOS=(
    ("f","Fácil"),
    ("m", "Médio"),
    ("d" , "Dificil"),
    
)
class Jogo(models.Model):
    nome = models.CharField("Nome do jogo:", max_length=100, blank=False, null=False)
    qtd_jogadores = models.PositiveIntegerField("Quantidades de jogadores:", blank=False, null=False)
    nivel_jogo = models.CharField("Nível do jogo:", max_length=90, choices=NIVEL_JOGO, blank=False, null=False)

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
        db_table = "new_game_jogo"

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome_completo = models.CharField("Nome completo do jogador:", max_length=20, null=False, blank=False)
    pontuacao = models.IntegerField("Pontuação:", null=False, default=0)
    jogo = models.ForeignKey(Jogo,on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"
        db_table = "new_game_jogador"

    def __str__(self):
        return self.nome_completo


class Desafios(models.Model):
    frase = models.CharField("Desafios:", max_length=500, null=False, blank=False)
    nivel_frase = models.CharField("Nível da frase:", max_length=90, choices=NIVEL_DESAFIOS, blank=False, null=False)

    class Meta:
        verbose_name = "Desafio"
        verbose_name_plural = "Desafios"
        db_table = "new_game_desafios"

    def __str__(self):
        return self.frase


class Qtd_doses(models.Model):
    frase = models.CharField("Qtd_doses:", max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = "Qtd_dose"
        verbose_name_plural = "Qtd_doses"
        db_table = "new_game_Qtd_dose"

    def __str__(self):
        return self.frase


class RegraCasa(models.Model):
    frase = models.CharField("Regras da casa:", max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = "Regra_da_casa"
        verbose_name_plural = "Regras_da_casa"
        db_table = "new_game_regra_casa"

    def __str__(self):
        return self.frase
