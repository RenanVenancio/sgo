# Generated by Django 2.0.4 on 2019-06-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_auto_20190613_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='dataCadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro'),
        ),
    ]
