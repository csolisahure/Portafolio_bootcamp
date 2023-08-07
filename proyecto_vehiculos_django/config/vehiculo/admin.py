from django.contrib import admin
from django.contrib.auth.models import User, Permission
from . import models
from . models import Vehiculo

# Register your models here.

# Permite visualizar en la consola de Django Admin el catálogo de vehiculos. 
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio')

admin.site.unregister(User) # Importante

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'agregar_vehiculo', 'listar_vehiculo')
    
    # Permite visualizar en la consola de Django Admin los privilegios de usuarios. 
    @admin.display(boolean=True)
    def agregar_vehiculo(self, obj):
        return obj.has_perm("vehiculo.add_vehiculo")
    
    # Permite visualizar en la consola de Django Admin los privilegios de usuarios. 
    @admin.display(boolean=True)
    def listar_vehiculo(self, obj):
        #return obj.has_perm("vehiculo.list_vehiculo")
        #return obj.has_perm("APP_vehiculo.MODELO_listar_vehiculo")
        return obj.has_perm("vehiculo.view_vehiculo")


