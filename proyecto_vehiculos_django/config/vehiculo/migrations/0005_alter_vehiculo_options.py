# Generated by Django 4.2.3 on 2023-07-24 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculo_fecha_creacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': (('visualizar_catalogo', 'Visualizar Catálogo de Vehiculos'),), 'verbose_name_plural': 'Venta de Vehículos'},
        ),
    ]
