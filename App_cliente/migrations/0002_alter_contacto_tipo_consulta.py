# Generated by Django 4.0.4 on 2022-05-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencias'], [3, 'Felicitaciones']]),
        ),
    ]