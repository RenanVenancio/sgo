# Generated by Django 2.0.4 on 2019-05-26 00:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20190522_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamento',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blocos', to='sistema.Bloco', verbose_name='Bloco'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='prioridade',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Prioridade'),
        ),
    ]