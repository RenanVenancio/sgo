# Generated by Django 2.0.4 on 2019-06-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0018_auto_20190620_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagemUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='sistema/chamados', verbose_name='Envie uma foto')),
            ],
        ),
        migrations.AlterField(
            model_name='chamado',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='sistema/chamados', verbose_name='Envie uma foto'),
        ),
    ]
