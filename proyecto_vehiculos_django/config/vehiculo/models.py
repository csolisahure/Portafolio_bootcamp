from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Vehiculo(models.Model):
    marca = (
        ('FIAT', 'Fiat'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('TOYOTA', 'Toyota'),        
    )
    marca = models.CharField(max_length=20, default='FORD', choices=marca)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = (
        ('PARTICULAR','Particular'),
        ('TRANSPORTE','Transporte'),
        ('CARGA','Carga'),
    )
    categoria = models.CharField(max_length=20, default='Particular', choices=categoria)
    precio = models.IntegerField ()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta():
        #permiso "visualizar_catalogo"
        permissions = (
            ('visualizar_catalogo','Visualizar Catálogo de Vehículos'),
        )
        verbose_name_plural = 'Venta de Vehículos'

        def __str__(self):
            return self.permissions

