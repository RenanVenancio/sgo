# Generated by Django 2.0.4 on 2019-05-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0018_auto_20190521_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloco',
            name='empreendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema.Empreendimento', verbose_name='Empreendimento'),
        ),
    ]
