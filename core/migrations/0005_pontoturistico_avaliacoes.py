# Generated by Django 4.0.6 on 2022-07-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
    ]
