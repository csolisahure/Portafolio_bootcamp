# Generated by Django 4.2.3 on 2023-07-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculo_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
