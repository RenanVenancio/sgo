# Generated by Django 2.0.4 on 2019-06-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0022_auto_20190623_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='novosEventos',
            field=models.BooleanField(default=False, verbose_name='Novos eventos disponíveis'),
        ),
    ]
