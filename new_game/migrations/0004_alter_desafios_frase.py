# Generated by Django 3.2 on 2021-04-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_game', '0003_desafios_qtd_doses_regracasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desafios',
            name='frase',
            field=models.CharField(max_length=500, verbose_name='Desafios:'),
        ),
    ]
