from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

#admin.site.register(Laboratorio)
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')


#admin.site.register(DirectorGeneral)
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
        list_display = ('id', 'nombre', 'laboratorio', 'especialidad')


#admin.site.register(Producto)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
            list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
            list_filter = ('nombre', 'laboratorio')
