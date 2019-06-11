# Generated by Django 2.0.4 on 2019-06-11 03:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20190611_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='inicioGarantia',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de interação'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='feedbackUsuario',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Feedback dado pelo Usuário'),
        ),
    ]