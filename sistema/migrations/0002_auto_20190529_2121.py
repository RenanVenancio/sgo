# Generated by Django 2.0.4 on 2019-05-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventoschamado',
            name='descicaoEvento',
        ),
        migrations.AddField(
            model_name='eventoschamado',
            name='descricaoEvento',
            field=models.CharField(default=1, max_length=90, verbose_name='Evento'),
            preserve_default=False,
        ),
    ]