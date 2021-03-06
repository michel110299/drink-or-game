# Generated by Django 3.2 on 2021-04-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_game', '0002_alter_jogador_pontuacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desafios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.CharField(max_length=20, verbose_name='Desafios:')),
                ('nivel_frase', models.CharField(choices=[('f', 'Fácil'), ('m', 'Médio'), ('d', 'Dificil'), ('xtd', 'X-tudo')], max_length=90, verbose_name='Nível da frase:')),
            ],
            options={
                'verbose_name': 'Desafio',
                'verbose_name_plural': 'Desafios',
                'db_table': 'new_game_desafios',
            },
        ),
        migrations.CreateModel(
            name='Qtd_doses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.CharField(max_length=20, verbose_name='Qtd_doses:')),
            ],
            options={
                'verbose_name': 'Qtd_dose',
                'verbose_name_plural': 'Qtd_doses',
                'db_table': 'new_game_Qtd_dose',
            },
        ),
        migrations.CreateModel(
            name='RegraCasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.CharField(max_length=20, verbose_name='Regras da casa:')),
            ],
            options={
                'verbose_name': 'Regra_da_casa',
                'verbose_name_plural': 'Regras_da_casa',
                'db_table': 'new_game_regra_casa',
            },
        ),
    ]
